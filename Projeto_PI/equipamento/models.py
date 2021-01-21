from django.db import models
 
class Fornecedor(models.Model):  
    nome = models.CharField(max_length=100)  
    email = models.CharField(max_length=100)
    endereco = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    regiao = models.CharField(max_length=100)
    cep = models.CharField(max_length=100)
    pais = models.CharField(max_length=100)
    telefone = models.CharField(max_length=100) 
    class Meta:  
        db_table = "fornecedor"
        
class Area(models.Model):  
    nome = models.CharField(max_length=100)  
    class Meta:  
        db_table = "area"
        
class Salas(models.Model):  
    codigo = models.CharField(max_length=100)
    area = models.ForeignKey(Area, on_delete=models.CASCADE, null=True)
    class Meta:  
        db_table = "salas"
        
class Responsavel(models.Model):  
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=100)
    matricula = models.CharField(max_length=100)
    area = models.ForeignKey(Area, on_delete=models.CASCADE, null=True)
    class Meta:  
        db_table = "responsavel"
        
class EquipamentosFixos(models.Model):  
    eid = models.CharField(max_length=20)  
    ename = models.CharField(max_length=100)  
    emanutencao = models.BooleanField() 
    efornecedor = models.CharField(max_length=100)
    estatus = models.CharField(max_length=20)
    edataC = models.DateField() 
    edataM = models.DateField()
    earea = models.CharField(max_length=20)
    eqtd = models.PositiveIntegerField()
    #area = models.ForeignKey(Area, on_delete=models.CASCADE, null=True)
    #fornecedor = models.ForeignKey(Fornecedor, on_delete=models.CASCADE, null=True)
    class Meta:  
        db_table = "equipamentosFixos"  
        
class Alocacao(models.Model):  
    codigo = models.CharField(max_length=100)
    equipamento = models.ForeignKey(EquipamentosFixos, on_delete=models.CASCADE, null=True) 
    sala = models.ForeignKey(Salas, on_delete=models.CASCADE, null=True)
    data = models.DateField()
    horario = models.TimeField()
    horarioF = models.TimeField()
    responsavel = models.ForeignKey(Responsavel, on_delete=models.CASCADE, null=True)
    status = models.CharField(max_length=100) 
    class Meta:  
        db_table = "alocacao"
        
class Equipamento(models.Model):  
    eid = models.CharField(max_length=20)  
    ename = models.CharField(max_length=100)   
    edataC = models.DateField()
    estatus = models.CharField(max_length=20)
    efornecedor = models.CharField(max_length=100)
    earea = models.CharField(max_length=50)
    eqtd = models.PositiveIntegerField()
    #area = models.ForeignKey(Area, on_delete=models.CASCADE, null=True)
    #fornecedor = models.ForeignKey(Fornecedor, on_delete=models.CASCADE, null=True)
    class Meta:  
        db_table = "equipamento"
        
class Manutencao(models.Model):  
    eid = models.CharField(max_length=20)  
    equipamento = models.ForeignKey(EquipamentosFixos, on_delete=models.CASCADE, null=True)
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.CASCADE, null=True)
    edata = models.DateField()
    horario = models.TimeField()
    dias = models.PositiveIntegerField()
    status = models.CharField(max_length=20)
    class Meta:  
        db_table = "manutencao"
        
        

               

