# Python slim imajı
FROM python:3.13-slim

# Gerekli sistem paketlerini yükle
RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*

# Çalışma dizinini ayarla
WORKDIR /app

# Dosyaları kopyala
COPY . .

# Python bağımlılıklarını kur
RUN pip install --no-cache-dir -r requirements.txt

# Flask uygulamasını başlat
CMD ["flask", "run", "--host=0.0.0.0"]
