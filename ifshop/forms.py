from django import forms
from django.forms import modelformset_factory
from .models import Camiseta, Pedido, UsuarioCustomizado, ImagemCamiseta, EstiloTamanho
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


######################## login e cadastro de usuario  #############################       
        
class CadastroUsuarioForm(UserCreationForm):
    curso = forms.ChoiceField(
        choices=Camiseta.CURSOS_OPCOES,
        widget=forms.Select(attrs={'class': 'form-select rounded-3 '}))
    
    nome = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control rounded-3 '}))
    
    email = forms.EmailField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control rounded-3 '}))
    
    password1 = forms.CharField(
        label="Digite uma senha",
        widget=forms.PasswordInput(attrs={'class': 'form-control rounded-3 '}))
    
    password2 = forms.CharField(
        label="Confirme a senha",
        widget=forms.PasswordInput(attrs={'class': 'form-control rounded-3 '}))
    
    telefone = forms.CharField(
        min_length=10,
        max_length=100,
        widget=forms.TextInput(attrs={'type': 'number', 'class': 'form-control rounded-3 ', 'placeholder': 'Ex.: 8499999999'}))
    
    class Meta:
        model = UsuarioCustomizado
        fields = ['nome', 'email', 'telefone', 'curso', 'password1', 'password2' ]
        
    
        
class LoginUsuarioForm(AuthenticationForm):
    username = forms.EmailField(label="Email",widget=forms.EmailInput(attrs={'class': 'form-control rounded-3 '}))
    password = forms.CharField(label="Senha",widget=forms.PasswordInput(attrs={'class': 'form-control rounded-3 '}))
    
### Filtro ###
class FiltroProdutoForm(forms.Form):
    turnos = forms.ChoiceField(
        choices=[
            ('', 'Todos os Turnos'),  
            ('matutino', 'Matutino'),
            ('vespertino', 'Vespertino'),
            ('noturno', 'Noturno')
        ],
        required=False,
        widget=forms.Select(attrs={'class': 'form-select form-select-sm d-inline p-2'})
    )
    cursos = forms.ChoiceField(
        choices=[
            ('', 'Todos os Cursos'),  
            ('infoweb', 'InfoWeb'),
            ('edific', 'Edific'),
            ('mamb', 'Mamb'),
            ('outro', 'Outro'),
        ],
        required=False,
        widget=forms.Select(attrs={'class': 'form-select form-select-sm d-inline p-2'})
    )

class FiltroProdutosForm(forms.Form):
    status = forms.ChoiceField(
        choices=[
            ('', 'Todos os Pedidos'),  
            ('Pendente', 'Pendente'),
            ('Pago Totalmente', 'Pago Totalmente'),
            ('Pago 1° Parcela', 'Pago 1° Parcela'),
            ('Negociando com Usuario', 'Negociando com Usuario'),
        ],
        required=False,
        widget=forms.Select(attrs={'class': 'form-select form-select-sm d-inline p-2'})
    )
    
### Filtro ###

class CamisetaForm(forms.ModelForm):
    tamanhos = forms.MultipleChoiceField(
        choices=Camiseta.TAMANHOS_OPCOES,
        label='Tamanhos',
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'}),
        required=False
    )

    estilos = forms.MultipleChoiceField(
        choices=Camiseta.ESTILOS_OPCOES,
        label='Estilos',
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'}),
        required=True
    )
    
    data_limite_pedidos = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control rounded-3 ',}), required=True)
    
    data_pag1 = forms.DateField(
        label="Data para pagamento",
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control rounded-3 ',}), required=True)
    
    data_pag2 = forms.DateField(
        label="Data para pagamento da segunda parcela",
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control rounded-3',}), required=False, )
    
    
    titulo = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control rounded-3','placeholder': 'Ex.: Camisa De InfoWeb4M...'}), required=True)
    
    preco = forms.DecimalField(
        label="Preço Total",
        widget=forms.NumberInput(attrs={'class': 'form-control rounded-3','placeholder': 'Ex.: 00,00'}), required=True)
    
    preco_parcela = forms.DecimalField(
        label="Preço Parcelas",
        widget=forms.NumberInput(attrs={'class': 'form-control rounded-3','placeholder': 'Ex.: 00,00'}), required=False)
    
    forma_pag_op = forms.MultipleChoiceField(
        choices=Camiseta.FORMA_PAG_OPCOES,
        label= 'Formas de Pagamento Disponivel' ,
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'd-inline-block form-check-input '}), required=True)
    
    cursos = forms.ChoiceField(
        choices=Camiseta.CURSOS_OPCOES,
        widget=forms.Select(attrs={'class': 'form-select rounded-3',}), required=True)
    
    turnos = forms.ChoiceField(
        choices=Camiseta.TURNOS_OPCOES,
        widget=forms.Select(attrs={'class': 'form-select rounded-3',}), required=True)
    
    pix_qr_code_total = forms.ImageField(
        label= "Imagem Do QrCode Total",
        widget=forms.FileInput(attrs={'class': 'form-control'}), required= False
    )
    pix_qr_code_parcela = forms.ImageField(
        label= "Imagem Do QrCode Parcela",
        widget=forms.FileInput(attrs={'class': 'form-control'}), required= False
    )
    pix_chave_total = forms.CharField(
        label= "Coloque a chave pix para o pagamento",
        widget = forms.TextInput(attrs={'class': 'form-control'}), required= False
    )
    pix_chave_parcela = forms.CharField(
        label= "Coloque a chave pix para o pagamento",
        widget = forms.TextInput(attrs={'class': 'form-control'}), required= False
    )
    
    class Meta:
        model = Camiseta
        fields = ['titulo', 'preco', 'preco_parcela', 'forma_pag_op', 'cores', 'data_limite_pedidos', 'cursos', 
                  'turnos', 'tamanhos', 'estilos', "pix_qr_code_parcela", "pix_qr_code_total", "pix_chave_parcela", "pix_chave_total",
                  "data_pag1", "data_pag2"]
        widgets = {
            'cores': forms.TextInput(attrs={'placeholder': 'Ex: azul, vermelho, verde'})
        }
       
    def clean(self):
        cleaned_data = super().clean()
        estilos = cleaned_data.get("estilos", [])
        tamanhos_por_estilo = {}

        for estilo in estilos:
            tamanhos = self.data.getlist(f"tamanhos_{estilo}")
            if tamanhos:
                tamanhos_por_estilo[estilo] = tamanhos

        cleaned_data['tamanhos'] = tamanhos_por_estilo
        return cleaned_data   
        
    def save(self, commit=True):
        camiseta = super().save(commit=False)
        
        # `tamanhos` já deve vir como dicionário { estilo: [tamanhos] }
        camiseta.tamanhos = self.cleaned_data['tamanhos']
        camiseta.estilos = ", ".join(self.cleaned_data['estilos'])

        if commit:
            camiseta.save()
            # Limpar estilos anteriores e recriar
            EstiloTamanho.objects.filter(camiseta=camiseta).delete()
            for estilo, tamanhos in self.cleaned_data['tamanhos'].items():
                for tamanho in tamanhos:
                    EstiloTamanho.objects.create(
                        camiseta=camiseta,
                        estilo=estilo,
                        tamanho=tamanho
                    )
        return camiseta

    
ImagemCamisetaFormSet = modelformset_factory(
    ImagemCamiseta ,
    fields=('imagem', 'principal'),
    extra=4,  # Permite adicionar até 5 imagens por vez
    can_delete=True,
    widgets={
        'imagem': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        'principal': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
    }
)
####################################################################################################      

class PedidoForm(forms.ModelForm):
    cor_escolhida = forms.ChoiceField(label="Escolha a cor", choices=[], required=True)
    
    comprovante_total = forms.ImageField(
        label= "Anexe o Comprovante",
        widget=forms.FileInput(attrs={'class': 'form-control'}), required= False
    )
    
    comprovante_parcela1 = forms.ImageField(
        label= "Anexe o Comprovante da Primeira Parcela",
        widget=forms.FileInput(attrs={'class': 'form-control'}), required= False
    )
    
    comprovante_parcela2 = forms.ImageField(
        label= "Anexe o Comprovante da Segunda Parcela",
        widget=forms.FileInput(attrs={'class': 'form-control'}), required= False
    )
    
    nome_estampa = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'card-text mb-auto form-control',}))
    
    numero_estampa = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'card-text mb-auto form-control',}))
    
    tamanho = forms.ChoiceField(
        widget=forms.Select(attrs={'class': 'card-text mb-auto form-select', 'id': 'id_tamanho'}))
    
    estilo = forms.ChoiceField(
        widget=forms.Select(attrs={'class': 'card-text mb-auto form-select', 'id': 'id_estilo'}))
    
    forma_pag = forms.ChoiceField(
        label="Forma de Pagamento",
        widget=forms.Select(attrs={'class': 'card-text mb-auto form-select',}))

    class Meta:
        model = Pedido
        fields = ['nome_estampa', 'numero_estampa', 'tamanho', 'estilo', 'cor_escolhida', "forma_pag", "comprovante_total", "comprovante_parcela1", "comprovante_parcela2"]
        
    def __init__(self, *args, **kwargs):
        camiseta = kwargs.pop('camiseta', None)
        tamanhos_opcoes = kwargs.pop('tamanhos_opcoes', [])
        estilos_opcoes = kwargs.pop('estilos_opcoes', [])
        forma_pag_opcoes = kwargs.pop('forma_pag_opcoes', [])
        
        super().__init__(*args, **kwargs)

        self.fields['tamanho'].choices = [(op, op) for op in tamanhos_opcoes]
        self.fields['estilo'].choices = [(op, op) for op in estilos_opcoes]
        self.fields['forma_pag'].choices = [(op, op) for op in forma_pag_opcoes]
        
        if camiseta:
            cores_disponiveis = camiseta.lista_cores()
            print("Cores disponíveis:", cores_disponiveis)  # Verifique se as cores estão sendo passadas
            if cores_disponiveis:
                self.fields['cor_escolhida'].choices = [(cor, cor) for cor in cores_disponiveis]
            else:
                self.fields['cor_escolhida'].choices = [("", "Nenhuma cor disponível")]
        
class AlterarStatusPedidoForm(forms.ModelForm):
    status = forms.ChoiceField(choices=Pedido.STATUS_OPCOES, widget=forms.Select(attrs={'class': 'card-text mb-auto form-select',}))
    class Meta:
        model = Pedido
        fields = ['status']  # Apenas o campo de status

class AnexoComprovantesPedidoForm(forms.ModelForm):
    comprovante_total = forms.ImageField(
        label= "Anexe o Comprovante",
        widget=forms.FileInput(attrs={'class': 'form-control'}), required= False
    )
    
    comprovante_parcela1 = forms.ImageField(
        label= "Anexe o Comprovante da Primeira Parcela",
        widget=forms.FileInput(attrs={'class': 'form-control'}), required= False
    )
    
    comprovante_parcela2 = forms.ImageField(
        label= "Anexe o Comprovante da Segunda Parcela",
        widget=forms.FileInput(attrs={'class': 'form-control'}), required= False
    )
    class Meta:
        model = Pedido
        fields = ['comprovante_total','comprovante_parcela1','comprovante_parcela2']  # Apenas o campo de status 