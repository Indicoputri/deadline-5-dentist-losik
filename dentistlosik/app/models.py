from django.db import models

# Create your models here.
class doktergigi (models.Model):
    iddoktergigi = models.AutoField(primary_key = True)
    namadoktergigi =  models.CharField(max_length = 100)
    alamatdoktergigi =  models.CharField(max_length = 10)
    nohpdoktergigi =  models.IntegerField()

    def __str__(self) :
        return str (self.iddoktergigi)

class pasien (models.Model) :
    idpasien = models.AutoField(primary_key =True)
    namapasien = models.CharField(max_length=70)
    jeniskelamin = models.CharField(max_length = 15)
    alamatpasien = models.CharField(max_length = 15)   
    nohppasien = models.IntegerField()

    def __str__(self):
        return str (self.idpasien)

class pelayanan (models.Model):
    idpelayanan = models.AutoField(primary_key =True)
    namapelayanan = models.CharField(max_length=70)
    hargapelayanan = models.IntegerField()

    def __str__(self):
        return str (self.idpelayanan)


class pendaftaran (models.Model) :
    idpendaftaran = models.AutoField(primary_key =True)
    iddoktergigi = models.ForeignKey(doktergigi,max_length=50, on_delete=models.CASCADE)
    idpasien = models.ForeignKey(pasien,max_length=50, on_delete=models.CASCADE)
    tanggalpendaftaran= models.DateField()

    def __str__(self):
        return str (self.idpendaftaran)

class detailpelayanan (models.Model) :
    iddetailpelayanan = models.AutoField(primary_key = True)
    idpendaftaran = models.ForeignKey (pendaftaran, on_delete=models.CASCADE)
    idpelayanan = models.ForeignKey (pelayanan, on_delete=models.CASCADE)
    jumlahpelayanan = models.IntegerField()

    def __str__(self):
        return str (self.iddetailpelayanan)