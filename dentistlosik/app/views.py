from django.shortcuts import render, redirect
from . import models
from datetime import datetime

def home (request):
  pasienall = models.pasien.objects.all()

  return render(request,'home.html',{
    'pasien': pasienall
  })

# DOKTERGIGI
def doktergigi (request) : 
    doktergigiall = models.doktergigi.objects.all()

    return render (request, 'doktergigi.html', {
    'doktergigiall' : doktergigiall
    })


def updatedatadoktergigi (request, id) :
    # get specific object
    doktergigiobj = models.doktergigi.objects.get(iddoktergigi=id)
    if request.method == "GET" : 
        return render (request, 'updatedatadoktergigi.html', {
            'doktergigiobj' : doktergigiobj
        })
    else :
        doktergigiobj.namadoktergigi = request.POST['namadoktergigi']
        doktergigiobj.alamatdoktergigi = request.POST['alamatdoktergigi']
        doktergigiobj.nohpdoktergigi = request.POST['nohpdoktergigi']
        doktergigiobj.save()
        return redirect('doktergigi')

# PASIEN
def pasien(request) : 
    # READ
    # all data
    pasienall = models.pasien.objects.all()

    return render (request, 'pasien.html', {
        'pasienall' : pasienall
    })

def createdatapasien(request):
    if request.method == "GET":
        return render(request,'createdatapasien.html')
    else:
        namapasien = request.POST['namapasien']
        jeniskelamin = request.POST['jeniskelamin']
        alamatpasien = request.POST['alamatpasien']
        nohppasien = request.POST['nohppasien']

        newpelanggan = models.pasien(
            namapasien = namapasien,
            jeniskelamin = jeniskelamin,
            alamatpasien = alamatpasien,
            nohppasien = nohppasien
        ).save()
        return redirect('pasien')

def updatedatapasien (request, id) :
    # get specific object
    pasienobj = models.pasien.objects.get(idpasien=id)
    if request.method == "GET" : 
        return render (request, 'updatedatapasien.html', {
            'pasienobj' : pasienobj
        })
    else :
        pasienobj.namapasien = request.POST['namapasien']
        pasienobj.jeniskelamin= request.POST['jeniskelamin']
        pasienobj.alamatpasien = request.POST['alamatpasien']
        pasienobj.nohppasien = request.POST['nohppasien']
        pasienobj.save()
        return redirect('pasien')

def deletedatapasien(request,id):
    pasienobj = models.pasien.objects.get(idpasien = id)
    pasienobj.delete()
    return redirect('pasien')


#  PELAYANAN
def pelayanan(request) : 
    # READ
    # all data
    pelayananall = models.pelayanan.objects.all()

    return render (request, 'pelayanan.html', {
        'pelayanan' : pelayananall
    })

def createdatapelayanan(request):
    if request.method == "GET":
        return render(request, 'createdatapelayanan.html')
    else:
        namapelayanan = request.POST['namapelayanan']
        hargapelayanan = request.POST['hargapelayanan']

        newpelayanan = models.pelayanan(
            namapelayanan = namapelayanan,
            hargapelayanan = hargapelayanan
        ).save()
        return redirect('pelayanan')

def updatedatapelayanan (request, id) :
    # get specific object
    pelayananobj = models.pelayanan.objects.get(idpelayanan=id)
    if request.method == "GET" : 
        return render (request, 'updatedatapelayanan.html', {
            'pelayananobj' : pelayananobj
        })
    else :
        pelayananobj.namapelayanan = request.POST['namapelayanan']
        pelayananobj.hargapelayanan= request.POST['hargapelayanan']
        pelayananobj.save()
        return redirect('pelayanan')

def deletedatapelayanan(request,id):
    pelayananobj = models.pasien.objects.get(idpasien = id)
    pelayananobj.delete()
    return redirect('pelayanan')

# PENDAFTARAN
def pendaftaran (request) : 
    pendaftaranall = models.pendaftaran.objects.all()
    return render (request, 'pendaftaran.html', {
        'pendaftaran' : pendaftaranall
        })
def createdatapendaftaran(request):
    doktergigiall = models.doktergigi.objects.all()
    pasienall = models.pasien.objects.all()

    if request.method == "GET":
        return render (request,'createdatapendaftaran.html',{
            'doktergigiall' : doktergigiall,
            'pasienall' : pasienall
            })
    else:
        iddoktergigi = request.POST['iddoktergigi']
        getdoktergigi = models.doktergigi.objects.get(iddoktergigi = iddoktergigi)
        idpasien = request.POST['idpasien']
        getpasien = models.pasien.objects.get(idpasien = idpasien)
        doktergigiobj = getdoktergigi
        pasienobj = getpasien
        tanggalpendaftaran = request.POST['tanggalpendaftaran']

        newpendaftaran = models.pendaftaran(
            iddoktergigi = doktergigiobj,
            idpasien=pasienobj,
            tanggalpendaftaran = tanggalpendaftaran
            ).save()
        return redirect('pendaftaran')

def updatedatapendaftaran (request,id):
    pendaftaranobj = models.pendaftaran.objects.get(idpendaftaran = id)
    doktergigiall = models.doktergigi.objects.all()
    pasienall = models.pasien.objects.all()
    tanggalpendafataran = datetime.strftime(pendaftaranobj.tanggalpendaftaran, '%m-%d-%Y')
    if request.method =="GET":
        return render(request,'updatedatapendaftaran.html',{
        'pendaftaran' : pendaftaranobj,
        'doktergigiall' : doktergigiall,
        'pasienall' : pasienall,
        'tanggalpendaftaran' : tanggalpendafataran
    })
    else:
        pendaftaranobj.doktergigi = request.POST['iddoktergigi']
        doktergigibaru = models.doktergigi.objects.get(iddoktergigi = request.POST['iddoktergigi'])
        pendaftaranobj.iddoktergigi = doktergigibaru
        pendaftaranobj.pasien = request.POST['idpasien']
        pasienbaru = models.pasien.objects.get(idpasien = request.POST ['idpasien'])
        pendaftaranobj.idpasien = pasienbaru
        pendaftaranobj.tanggalpendaftaran = request.POST['tanggalpendaftaran']
        pendaftaranobj.save()
        return redirect('pendaftaran')

# DETAILPELAYANAN
def detailpelayanan (request) : 
    detailpelayananall = models.detailpelayanan.objects.all()
    return render (request, 'detailpelayanan.html', {
        'detailpelayanan' : detailpelayananall
        })
def createdatadetailpelayanan(request):
    pendaftaranall = models.pendaftaran.objects.all()
    pelayananall = models.pelayanan.objects.all()

    if request.method == "GET":
        return render (request,'createdatadetailpelayanan.html',{
            'pendaftaranall' : pendaftaranall,
            'pelayananall' : pelayananall
            })
    else:
        idpendaftaran = request.POST['idpendaftaran']
        getpendaftaran = models.pendaftaran.objects.get(idpendaftaran = idpendaftaran)
        idpelayanan = request.POST['idpelayanan']
        getpelayanan = models.pelayanan.objects.get(idpelayanan = idpelayanan)
        pendaftaranobj = getpendaftaran
        pelayananobj = getpelayanan
        jumlahpelayanan = request.POST['jumlahpelayanan']

        newdetailpelayanan = models.detailpelayanan(
            idpendaftaran = pendaftaranobj,
            idpelayanan = pelayananobj,
            jumlahpelayanan = jumlahpelayanan
            ).save()
        return redirect('detailpelayanan')

def updatedatadetailpelayanan(request,id):
    detailpelayananobj = models.detailpelayanan.objects.get(iddetailpelayanan = id)
    pendaftaranall = models.pendaftaran.objects.all()
    pelayananall = models.pelayanan.objects.all()


    if request.method =="GET":
        return render(request,'updatedatadetailpelayanan.html',{
        'detailpelayanan' : detailpelayananobj,
        'pendaftaranall' : pendaftaranall,
        'pelayananall' : pelayananall,

    })
    else:
        detailpelayananobj.pendaftaran = request.POST['idpendaftaran']
        pendaftaranbaru = models.pendaftaran.objects.get(idpendaftaran = request.POST['idpendaftaran'])
        detailpelayananobj.idpendaftaran = pendaftaranbaru
        detailpelayananobj.pelayanan = request.POST['idpelayanan']
        pelayananbaru = models.pelayanan.objects.get(idpelayanan = request.POST ['idpelayanan'])
        detailpelayananobj.idpelayanan = pelayananbaru
        detailpelayananobj.jumlahpelayanan = request.POST['jumlahpelayanan']

        detailpelayananobj.save()
        return redirect('detailpelayanan')
