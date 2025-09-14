import pandas as pd
import json
from datetime import datetime
import os

def csv_to_javascript(csv_file, js_file):
    """경제성 계산 툴 CSV를 JavaScript 파일로 변환"""
    
    print(f"📊 CSV 파일 로드 중: {csv_file}")
    
    # CSV 로드
    df = pd.read_csv(csv_file)
    
    print(f"✅ CSV 로드 완료: {len(df):,}개 행")
    print(f"📋 컬럼: {list(df.columns)}")
    
    # 데이터를 JavaScript 배열로 변환
    data_records = df.to_dict('records')
    
    # 통계 정보 생성
    stats = {
        'total_records': len(df),
        'categories': df['category'].nunique() if 'category' in df.columns else 0,
        'products': df['product'].nunique() if 'product' in df.columns else 0,
        'date_range': {
            'start': df['date'].min() if 'date' in df.columns else 'N/A',
            'end': df['date'].max() if 'date' in df.columns else 'N/A'
        },
        'price_range': {
            'min': float(df['price'].min()) if 'price' in df.columns else 0,
            'max': float(df['price'].max()) if 'price' in df.columns else 0,
            'avg': float(df['price'].mean()) if 'price' in df.columns else 0
        }
    }
    
    # JavaScript 파일 생성
    js_content = f'''// 경제성 계산 툴 데이터
// 생성일: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
// 총 {len(df):,}개 데이터
// 원본 CSV: {os.path.basename(csv_file)}

const PRICE_DATA = {json.dumps(data_records, ensure_ascii=False, indent=2)};

// 데이터 통계
const DATA_STATS = {json.dumps(stats, ensure_ascii=False, indent=2)};

// 데이터 접근 함수들
function getPriceData() {{
    return PRICE_DATA;
}}

function getDataStats() {{
    return DATA_STATS;
}}

function getCategories() {{
    return [...new Set(PRICE_DATA.map(item => item.category))].sort();
}}

function getProducts() {{
    return [...new Set(PRICE_DATA.map(item => item.product))].sort();
}}

function getProductsByCategory(category) {{
    return PRICE_DATA
        .filter(item => item.category === category)
        .map(item => item.product)
        .filter((value, index, self) => self.indexOf(value) === index)
        .sort();
}}

function getPriceHistory(category, product) {{
    return PRICE_DATA
        .filter(item => item.category === category && item.product === product)
        .sort((a, b) => new Date(a.date_full) - new Date(b.date_full));
}}

function getLatestPrice(category, product) {{
    const history = getPriceHistory(category, product);
    return history.length > 0 ? history[history.length - 1] : null;
}}

function getPriceByDate(category, product, date) {{
    return PRICE_DATA.find(item => 
        item.category === category && 
        item.product === product && 
        item.date === date
    );
}}

// 데이터 검증 함수
function validateData() {{
    const issues = [];
    
    // 빈 값 체크
    const emptyValues = PRICE_DATA.filter(item => 
        !item.category || !item.product || !item.price
    );
    if (emptyValues.length > 0) {{
        issues.push(`빈 값이 있는 레코드: ${{emptyValues.length}}개`);
    }}
    
    // 가격 범위 체크
    const invalidPrices = PRICE_DATA.filter(item => 
        item.price <= 0 || item.price > 10000000
    );
    if (invalidPrices.length > 0) {{
        issues.push(`비정상적인 가격: ${{invalidPrices.length}}개`);
    }}
    
    return {{
        isValid: issues.length === 0,
        issues: issues,
        totalRecords: PRICE_DATA.length
    }};
}}

console.log('📊 경제성 계산 데이터 로드 완료:', PRICE_DATA.length, '개');
console.log('📈 데이터 통계:', DATA_STATS);
console.log('🔍 데이터 검증:', validateData());
'''
    
    # JavaScript 파일 저장
    with open(js_file, 'w', encoding='utf-8') as f:
        f.write(js_content)
    
    print(f"✅ 변환 완료: {len(df):,}개 → {js_file}")
    
    # 파일 크기 확인
    file_size = os.path.getsize(js_file)
    print(f"📁 생성된 파일 크기: {file_size:,} bytes ({file_size/1024/1024:.1f} MB)")
    
    # 데이터 검증
    validation = {
        'total_records': len(df),
        'categories': df['category'].nunique() if 'category' in df.columns else 0,
        'products': df['product'].nunique() if 'product' in df.columns else 0,
        'date_range': f"{df['date'].min()} ~ {df['date'].max()}" if 'date' in df.columns else 'N/A',
        'price_range': f"{df['price'].min():,.0f} ~ {df['price'].max():,.0f}" if 'price' in df.columns else 'N/A'
    }
    
    print("📊 데이터 요약:")
    for key, value in validation.items():
        print(f"  {key}: {value}")

if __name__ == "__main__":
    # 파일 경로 설정
    csv_file = "../dcf-backup/price_data_processed.csv"
    js_file = "js/price-data.js"
    
    # js 폴더 생성
    os.makedirs("js", exist_ok=True)
    
    # CSV 파일 존재 확인
    if not os.path.exists(csv_file):
        print(f"❌ CSV 파일을 찾을 수 없습니다: {csv_file}")
        print("📁 사용 가능한 CSV 파일들:")
        for root, dirs, files in os.walk(".."):
            for file in files:
                if file.endswith(".csv"):
                    print(f"  - {os.path.join(root, file)}")
        exit(1)
    
    # JavaScript 파일 생성
    csv_to_javascript(csv_file, js_file)
    
    print("\n🎉 변환 완료!")
    print("📝 다음 단계:")
    print("1. js/price-data.js 파일이 생성되었습니다")
    print("2. HTML에서 이 파일을 로드하도록 수정합니다")
    print("3. 기존 CSV 로딩 코드를 JavaScript 데이터 사용으로 변경합니다")
    print("4. Git에 업로드합니다 (CSV 파일은 제외)")
