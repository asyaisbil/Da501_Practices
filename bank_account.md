Q1 – Banka hesap hareketleri
Zorluk: Orta-Zor · Odak: while + komut ayrıştırma, çoklu koşul, sayaçlar

İlk satırda başlangıç bakiyesi gelir. Sonraki her satır bir komuttur; BITIR gelene kadar okumaya devam et (büyük/küçük harf duyarsız).

Komut	Davranış
YATIR x	Bakiyeye x ekle
CEK x	x > bakiye ise Yetersiz bakiye. Gün içi toplam çekim 5000'i aşacaksa Limit asildi. Aksi halde çek
FAIZ r	Bakiyeyi %r artır
Diğer / eksik parametre	Gecersiz komut
Tutar ≤ 0 ise Gecersiz tutar yazdır.
Reddedilen her işlem (geçersiz komut dahil) reddedilen sayacını artırır.
Sayısal parametrelerin sayıya çevrilebilir olduğunu varsay.
Döngü bitince şunları yazdır (2 ondalık, format(x, ".2f")):

Örnek girdi: 1000, YATIR 500, CEK 2000, cek 1200, FAIZ 10, HAVALE 5, YATIR 6000, CEK 4000, YATIR -50, BITIR
