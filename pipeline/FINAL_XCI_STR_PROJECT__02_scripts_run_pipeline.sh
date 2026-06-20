#!/bin/bash
# اجرای کامل pipeline پروژه XCI_STR

set -e

echo "==========================================="
echo "   Pipeline اجرای پروژه XCI_STR"
echo "==========================================="
echo "تاریخ شروع: $(date)"
echo ""

# تابع اجرای مرحله
run_step() {
    local step_num=$1
    local step_name=$2
    local script_dir=$3
    
    echo ""
    echo "🔄 مرحله ${step_num}: ${step_name}"
    echo "   پوشه: ${script_dir}"
    echo "   شروع: $(date '+%H:%M:%S')"
    
    if [ -d "${script_dir}" ]; then
        # پیدا کردن اسکریپت اصلی (با پیشوند 01_)
        main_script=$(find "${script_dir}" -name "01_*" -type f | head -1)
        
        if [ -n "${main_script}" ] && [ -f "${main_script}" ]; then
            echo "   🚀 اجرای: $(basename ${main_script})"
            
            if [[ "${main_script}" == *.sh ]]; then
                bash "${main_script}"
                exit_code=$?
            elif [[ "${main_script}" == *.py ]]; then
                python "${main_script}"
                exit_code=$?
            else
                echo "   ⚠️  نوع فایل نامشخص: ${main_script}"
                exit_code=1
            fi
            
            if [ $exit_code -eq 0 ]; then
                echo "   ✅ انجام شد: ${step_name}"
            else
                echo "   ❌ خطا در اجرا: ${step_name}"
                exit $exit_code
            fi
        else
            echo "   ⚠️  اسکریپت اصلی یافت نشد. ادامه..."
        fi
    else
        echo "   ⚠️  پوشه وجود ندارد. ادامه..."
    fi
    
    echo "   پایان: $(date '+%H:%M:%S')"
}

# اجرای مراحل اصلی
run_step "01" "آماده‌سازی داده" "01_data_preparation"
run_step "02" "اجرای TRF" "02_trf_execution"
run_step "03" "استخراج داده‌ها" "03_data_extraction"
run_step "04" "تحلیل اصلی STR" "04_str_analysis_main"
run_step "05" "فیلتر و کنترل کیفیت" "05_data_filtering_qc"
run_step "08" "مصورسازی" "08_visualization"
run_step "09" "گزارش‌گیری" "09_reporting"

echo ""
echo "==========================================="
echo "   Pipeline با موفقیت اجرا شد!"
echo "==========================================="
echo "تاریخ پایان: $(date)"
echo ""
echo "📁 نتایج در پوشه‌های زیر ذخیره شدند:"
echo "   - analysis_results/ (نتایج تحلیل اصلی)"
echo "   - results/ (نتایج میانی)"
echo "   - data/processed/ (داده‌های پردازش شده)"
echo ""
echo "📊 برای مشاهده نتایج:"
echo "   cat analysis_results/basic_statistics.csv"
echo "   cat analysis_results/x_vs_autosomes_comparison.csv"
echo ""
echo "🔍 برای بررسی وضعیت پروژه:"
echo "   python 10_utilities/check_project_status.py"
