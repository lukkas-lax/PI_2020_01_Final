from django.shortcuts import render
from django.shortcuts import render, redirect  
from equipamento.forms import EquipamentoForm
from equipamento.forms import EquipamentosFixosForm
from equipamento.forms import AlocacaoForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import mysql.connector
from equipamento.models import Equipamento  
from equipamento.models import EquipamentosFixos
from equipamento.models import Alocacao
from equipamento.models import Manutencao
from datetime import *
from pi.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
# Create your views here.  

@login_required(login_url='/login/')
def emp(request):  
    if request.method == "POST":  
        form = EquipamentoForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/show')  
            except:  
                pass  
    else:  
        form = EquipamentoForm()  
    return render(request,'index.html',{'form':form})  


@login_required(login_url='/login/')
def empf(request):  
    if request.method == "POST":  
        form = EquipamentosFixosForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/showf')  
            except:  
                pass  
    else:  
        form = EquipamentosFixosForm()  
    return render(request,'indexf.html',{'form':form}) 


@login_required(login_url='/login/')
def empAloc(request):  
    if request.method == "POST":  
        form = AlocacaoForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/showAloc')  
            except:  
                pass  
    else:  
        form = AlocacaoForm()  
    return render(request,'indexAloc.html',{'form':form}) 


@login_required(login_url='/login/')
def show(request):  
    equipamentos = Equipamento.objects.all()  
    return render(request,"show.html",{'equipamentos':equipamentos}) 


@login_required(login_url='/login/')
def showf(request):  
    equipamentos = EquipamentosFixos.objects.all()  
    return render(request,"showf.html",{'equipamentos':equipamentos})


@login_required(login_url='/login/')
def showAloc(request):  
    equipamentos = Alocacao.objects.all()  
    return render(request,"showAloc.html",{'equipamentos':equipamentos}) 

@login_required(login_url='/login/')
def showMan(request):  
    equipamentos = Manutencao.objects.all()  
    return render(request,"showMan.html",{'equipamentos':equipamentos}) 


@login_required(login_url='/login/')
def edit(request, id):  
    equipamento = Equipamento.objects.get(id=id)  
    return render(request,'edit.html', {'equipamento':equipamento}) 

@login_required(login_url='/login/')
def det(request, id):  
    equipamento = Manutencao.objects.get(id=id)  
    return render(request,'detalhes.html', {'equipamento':equipamento}) 


@login_required(login_url='/login/')
def editf(request, id):  
    equipamento = EquipamentosFixos.objects.get(id=id)  
    return render(request,'editf.html', {'equipamento':equipamento})


@login_required(login_url='/login/')
def update(request, id):  
    equipamento = Equipamento.objects.get(id=id)  
    form = EquipamentoForm(request.POST, instance = equipamento)  
    if form.is_valid():  
        form.save()  
        return redirect("/show")  
    return render(request, 'edit.html', {'equipamento': equipamento})


@login_required(login_url='/login/')
def updatef(request, id):  
    equipamento = EquipamentosFixos.objects.get(id=id)  
    form = EquipamentosFixosForm(request.POST, instance = equipamento)  
    if form.is_valid():  
        form.save()  
        return redirect("/showf")  
    return render(request, 'editf.html', {'equipamento': equipamento})


@login_required(login_url='/login/')
def destroy(request, id):  
    equipamento = Equipamento.objects.get(id=id)  
    equipamento.delete()  
    return redirect("/show")


@login_required(login_url='/login/')
def destroyf(request, id):  
    equipamento = EquipamentosFixos.objects.get(id=id)  
    equipamento.delete()  
    return redirect("/showf") 


def login_user(request):
    return render(request, 'login.html')


def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username = username, password = password)
        if user is not None:
            login(request,user)
            return redirect("/show")
        else:
            messages.error(request, "Usuário ou senha incorretos!")
    return redirect('/login/')  


def logout_user(request):
    logout(request)
    return redirect('/login/')

def email(request,id):
    alocacao = Alocacao.objects.get(id=id)
    alocacao.status = 'Confirmado'
    alocacao.save()
    subject = 'Confirmação de Alocação'
    message = 'A alocação do equipamento: "' +alocacao.equipamento.ename+ '" foi confirmada com sucesso!\n Data: ' +str(alocacao.data)+ '\n Horário de Inicio: '+str(alocacao.horario)+ '\n Horário Fim: '+str(alocacao.horarioF)+ '\nSala: ' +alocacao.sala.codigo+ '\n\n Ayano Solutions!!!'
    recepient = 'lucasxavier.1050@aluno.saojudas.br'
    send_mail(subject, message, EMAIL_HOST_USER, [recepient], fail_silently = False)
    return redirect("/showAloc")  

def emailMan(request,id):
    manutencao = Manutencao.objects.get(id=id)
    manutencao.status = 'Agendado com Sucesso'
    manutencao.save()
    subject = 'Confirmação de Agendamento de Manutenção - ' + manutencao.eid
    message = 'A manutenção do equipamento: '+manutencao.equipamento.eid+' - '+manutencao.equipamento.ename+ ' foi agendada com sucesso.\n Dados da Manutenção:\n Data da Compra - '+str(manutencao.equipamento.edataC)+'\nQuantidade - '+str(manutencao.equipamento.eqtd)+'\n Fornecedor - '+manutencao.fornecedor.nome+'\n E-mail - '+manutencao.fornecedor.email+'\n Telefone - '+manutencao.fornecedor.telefone+'\n Data/Horario da Manutenção - '+str(manutencao.edata)+" / "+str(manutencao.horario)+ '\n\n Por Favor, entrar em contato com o fornecedor para proceder com a manutenção!!'
    recepient = 'lucasxavier.1050@aluno.saojudas.br'
    send_mail(subject, message, EMAIL_HOST_USER, [recepient], fail_silently = False)
    return redirect("/showMan")

def conc(request,id):
    manutencao = Manutencao.objects.get(id=id)
    ide = manutencao.id
    equipamento = EquipamentosFixos.objects.get(id=ide)
    d = manutencao.edata
    d = d + timedelta(days=90)
    manutencao.status = 'Prox. Manutenção'
    manutencao.edata = d
    equipamento.edataM = manutencao.edata
    equipamento.save()
    manutencao.save()
    return redirect("/showMan")   
    


