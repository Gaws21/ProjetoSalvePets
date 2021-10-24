from crispy_forms.helper import FormHelper
from crispy_forms.layout import Div, Field, Fieldset, Layout, Submit
from django import forms
from .models import Pet, USUARIO, User, ADOCAO, INSTITUICAO
#from .custom_form_fields import cpfcnpjField, TelefoneField
from django.utils.translation import ugettext_lazy as _



# Criar Array de Ano de Nascimento - não sei se faz sentido mover pra arquivo separado..

BIRTH_YEAR_CHOICES  = []
for i in range(1900,2021):
    BIRTH_YEAR_CHOICES.append(str(i))

# Forms - pra mim isso aqui é o "Controller" do projeto. Masterizar isso é garantia de sucesso.

class SignupForm(forms.Form):
    first_name = forms.CharField(max_length=30, label=_('Nome:'))
    last_name = forms.CharField(max_length=30, label=_('Sobrenome'))

    def signup(self, request, user):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()

class PetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = '__all__'



class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name')

class UsuarioForm(forms.ModelForm):
    #cpfcnpj = CpfcnpjField(label='CPF')
    #dataNascimento = forms.DateField(required=True, widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES),input_formats=['%d/%m/%Y','%m/%d/%Y'], label=_('Data de Nascimento'))
    dataNascimento = forms.DateField(required=True, widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES), label=_('Data de Nascimento'))
    #telefone = TelefoneField(required=False, label=_('Número de Telefone'))
    #receberNotificacoes = forms.BooleanField(required=False, label = 'Desejo receber notificações', help_text='(Marque este campo caso deseje ser notificado sobre pets perdidos ou encontrados.)')
    class Meta:
        model = USUARIO
        fields = ('cpfcnpj', 'dataNascimento', 'telefone', 'site', 'receberNotificacoes') #Retirei tipoUsuairo


#Classe que seria usada como "Cadastro Único" - li que é possível fazer funcionar, só preciso entender melhor como.
#Por enquanto não está implementada no Settings, então não é utilizada

class ExtendedSignupForm(SignupForm):
    cpfcnpj = forms.CharField(max_length=14, label='CPF')
    #dataNascimento = forms.DateField(required=True, widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES),input_formats=['%d/%m/%Y'], label=_('Data de Nascimento'))
    dataNascimento = forms.DateField(required=True, widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES), label=_('Data de Nascimento'))
    telefone = forms.CharField(required=False, max_length=16, label=_('Número de Telefone'))
    receberNotificacoes = forms.BooleanField(required=False, label = _('Desejo receber notificações'), help_text=_('(Marque este campo caso deseje ser notificado sobre pets perdidos ou encontrados.)'))
    #siteUrl = forms.URLField(initial='http://', label='URL do seu Site')





#Projeto integrado II
class ContactForm(forms.Form):
    nome_fantasia = forms.CharField(max_length = 50)
    razao_social = forms.CharField(max_length = 50)
    numero_cnpj = forms.CharField(max_length = 18)
    numero_telefone = forms.CharField(max_length = 16)
    email_address = forms.EmailField(max_length = 150)


class AdocaoForm(forms.ModelForm):
    class Meta:
        model = ADOCAO
        fields = '__all__'

class InstituicaoForm(forms.ModelForm):
    class Meta:
        model = INSTITUICAO
        fields = [
            'nome_instituicao',
            'razao_social',
            'cnpj',
            'telefone',
            'email',
            'postal_code',
            'address',
            'number',
            'complement',
            'district',
            'state',
            'city',
        ]
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "post"
        self.helper.form_action = "."
        self.helper.add_input(
            Submit(
                "submit",
                "Atualizar",
                css_class="btn btn-success btn-lg btn-block",
            )
        )
        self.helper.layout = Layout(
            Fieldset(
                "",
                "cnpj",
                "nome_instituicao",
                "razao_social",
                "telefone",
                "email",
                Div(
                    Field("postal_code", onchange="getAddress()", wrapper_class="col"),
                    Field("state", wrapper_class="col"),
                    Field("city", wrapper_class="col"),
                    css_class="row",
                ),
                Div(
                    Field("address", wrapper_class="col"),
                    Field("district", wrapper_class="col"),
                    css_class="row",
                ),
                Div(
                    Field("number", wrapper_class="col"),
                    Field("complement", wrapper_class="col"),
                    css_class="row",
                ),
                css_class="border-bottom mb-3",
            )
        )

class AdicionarUsuarioInstituicaoForm(forms.Form):
    cpf = forms.CharField(max_length=14)