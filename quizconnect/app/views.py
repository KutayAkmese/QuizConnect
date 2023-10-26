from django.shortcuts import render
kategori_liste=[
    "Fizik",
    "Kimya",
    "Biyoloji",
    "Matematik",
    "Turkce",
    "Cografya"
]
soru_grubu=[
    {
        "id":1,
        "name":"Biyoloji",
        "soru_adi":"Biyoloji Sorulari",
        "aciklama":"Biyoloji aciklama",
        "resim":"biyo.jpeg",
        "anasayfa":True
    },
    {
        "id":2,
        "name":"Cografya",
        "soru_adi":"Cografya Sorulari",
        "aciklama":"Cografya aciklama",
        "resim":"Cografya.jpeg",
        "anasayfa":True
    },
    {
        "id":3,
        "name":"Fizik",
        "soru_adi":"Fizik Sorulari",
        "aciklama":"Fizik aciklama",
        "resim":"Fizik.jpeg",
        "anasayfa":True
    },
    {
        "id":4,
        "name":"Kimya",
        "soru_adi":"Kimya Sorulari",
        "aciklama":"Kimya aciklama",
        "resim":"Kimya.jpeg",
        "anasayfa":True
    },
    {
        "id":5,
        "name":"Matematik",
        "soru_adi":"Matematik Sorulari",
        "aciklama":"Matematik aciklama",
        "resim":"mat.jpeg",
        "anasayfa":True
    },
    {
        "id":6,
        "name":"Turkce",
        "soru_adi":"Turkce Sorulari",
        "aciklama":"Turkce aciklama",
        "resim":"turkce.jpeg",
        "anasayfa":True
    },
]
def home(request):
    data={
        "kategoriler":kategori_liste
    }
    return render(request,"index.html",data)

def unterricht(request):
    data={
        "kategoriler":kategori_liste,
        "sorular":soru_grubu
    }
    return render(request,"dersler.html",data)

def unterrichtendetails(request,name):
    data={
        "name":name
    }
    return render(request,"details.html",data)