#!/bin/bash
# اجرای TRF برای کروموزوم‌های X و اتوزوم‌ها

echo "========================================="
echo "🧬 اجرای TRF برای Phase 5"
echo "========================================="

echo "پارامترهای TRF: 2 7 7 80 10 50 500"
echo ""

CHROMOSOMES=("chrX" "chr1" "chr19" "chr21" "chr8")

for chrom in "${CHROMOSOMES[@]}"; do
    echo "🔍 پردازش ${chrom}..."
    
    # بررسی وجود فایل FASTA
    if [ ! -f "data/raw/${chrom}.fa" ]; then
        echo "   ❌ فایل ${chrom}.fa یافت نشد"
        continue
    fi
    
    # بررسی اینکه آیا قبلاً اجرا شده
    trf_file="${chrom}.fa.2.7.7.80.10.50.500.dat"
    if [ -f "$trf_file" ]; then
        line_count=$(wc -l < "$trf_file" 2>/dev/null || echo 0)
        if [ "$line_count" -gt 1 ]; then
            echo "   ✅ قبلاً اجرا شده ($line_count خط)"
            continue
        fi
    fi
    
    # اجرای TRF
    echo "   ⚙️ در حال اجرای tandem repeats finder..."
    start_time=$(date +%s)
    
    ./trf409.linux64 "data/raw/${chrom}.fa" 2 7 7 80 10 50 500 -d -h 2>&1 | tail -5
    
    end_time=$(date +%s)
    duration=$((end_time - start_time))
    
    if [ $? -eq 0 ]; then
        echo "   ✅ TRF برای ${chrom} کامل شد (زمان: ${duration} ثانیه)"
        
        # بررسی خروجی
        if [ -f "${trf_file}" ]; then
            line_count=$(wc -l < "${trf_file}" 2>/dev/null || echo 0)
            if [ "$line_count" -gt 1 ]; then
                echo "   📊 تعداد خطوط: $line_count"
                
                # نمایش نمونه
                echo "   🧪 نمونه خط ۲:"
                sed -n '2p' "${trf_file}" 2>/dev/null | head -c 80
                echo "..."
            else
                echo "   ⚠️ فایل خروجی خالی است"
            fi
        else
            echo "   ❌ فایل خروجی ایجاد نشد"
        fi
    else
        echo "   ❌ خطا در اجرای TRF برای ${chrom}"
    fi
    
    echo ""
done

echo "========================================="
echo "📋 خلاصه فایل‌های TRF:"
ls -lh *.fa.2.7.7.80.10.50.500.dat 2>/dev/null | while read line; do
    echo "📄 $line"
done || echo "⚠️ هیچ فایل TRF یافت نشد"

echo -e "\n🎯 قدم بعدی: اجرای Phase 5"
echo "برای تحلیل: python phase5_analysis.py"
