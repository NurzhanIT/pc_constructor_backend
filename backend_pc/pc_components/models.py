from django.db import models
import uuid

# Create your models here.

# Create your models here.
class PcComponentModel(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    name = models.CharField(max_length=100, null=False)
    price = models.CharField(max_length=20, null=False)
    image = models.ImageField(upload_to='pc_components/images', null=True)
    UIDтовара = models.CharField(max_length=20, null=True)
    rating = models.IntegerField()

    def __str__(self):
        return self.name


class DetailInfoModel(models.Model):
    component = models.OneToOneField(PcComponentModel, on_delete=models.CASCADE, null=True , blank=True)
    #keyboard
    Производитель = models.CharField(max_length=20, null=True , blank=True)
    Модель = models.CharField(max_length=20, null=True , blank=True)
    Тип = models.CharField(max_length=20, null=True , blank=True)
    Типклавиатуры = models.CharField(max_length=20, null=True , blank=True)
    Цифровойблок = models.CharField(max_length=20, null=True , blank=True)
    Раскладкаклавиатуры = models.CharField(max_length=20, null=True , blank=True)
    Типклавиш = models.CharField(max_length=20, null=True , blank=True)
    Игровойрежим = models.CharField(max_length=20, null=True , blank=True)
    Типподключения = models.CharField(max_length=20, null=True , blank=True)
    Интерфейс = models.CharField(max_length=20, null=True , blank=True)
    Мышь = models.CharField(max_length=20, null=True , blank=True)
    Конструкциямыши = models.CharField(max_length=20, null=True , blank=True)
    Максимальноеразрешение = models.CharField(max_length=20, null=True , blank=True)
    Типсвязи = models.CharField(max_length=20, null=True , blank=True)
    Радиусдействия = models.CharField(max_length=20, null=True , blank=True)
    Цветиспользуемыйвоформлении = models.CharField(max_length=20, null=True , blank=True)
    Питание = models.CharField(max_length=20, null=True , blank=True)
    Материалкорпуса = models.CharField(max_length=20, null=True , blank=True)
    Размеры = models.CharField(max_length=20, null=True , blank=True)
    Весизделия = models.CharField(max_length=20, null=True , blank=True)
    Вессупаковкой = models.CharField(max_length=20, null=True , blank=True)
    Упаковка = models.CharField(max_length=20, null=True , blank=True)
    Срокгарантии = models.CharField(max_length=20, null=True , blank=True)
    Ссылканасайтпроизводителя = models.CharField(max_length=20, null=True , blank=True)
    #monitor
    Типматрицы = models.CharField(max_length=20, null=True , blank=True)
    Типповерхностиэкрана = models.CharField(max_length=20, null=True , blank=True)
    Диагональэкрана = models.CharField(max_length=20, null=True , blank=True)
    Соотношениесторон = models.CharField(max_length=20, null=True , blank=True)
    Размерпикселя = models.CharField(max_length=20, null=True , blank=True)
    Максимальноеразрешение = models.CharField(max_length=20, null=True , blank=True)
    Частотапримаксимальномразрешении = models.CharField(max_length=20, null=True , blank=True)
    Углыобзораэкранапогоризонтали = models.CharField(max_length=20, null=True , blank=True)
    Яркость = models.CharField(max_length=20, null=True , blank=True)
    ВремяоткликаматрицыMPRT = models.CharField(max_length=20, null=True , blank=True)
    Отображаемыецвета  = models.CharField(max_length=20, null=True , blank=True)
    Глубинацвета = models.CharField(max_length=20, null=True , blank=True)
    ЦветовойохватDCI = models.CharField(max_length=20, null=True , blank=True)
    VESADisplayHDR = models.CharField(max_length=20, null=True , blank=True)
    Интерфейсподключения = models.CharField(max_length=20, null=True , blank=True)
    Прочиеразъемы = models.CharField(max_length=20, null=True , blank=True)
    Цвет = models.CharField(max_length=20, null=True , blank=True)
    Потребляемаямощность = models.CharField(max_length=20, null=True , blank=True)
    СтандарткрепленияVESA = models.CharField(max_length=20, null=True , blank=True)
    СлотдлязамкаKensington = models.CharField(max_length=20, null=True , blank=True)
    Углынаклонамонитора = models.CharField(max_length=20, null=True , blank=True)
    Особенности = models.CharField(max_length=20, null=True , blank=True)
    Регулировкаповысоте = models.CharField(max_length=20, null=True , blank=True)
    Кабеливкомплекте = models.CharField(max_length=20, null=True , blank=True)
    Дополнительно = models.CharField(max_length=20, null=True , blank=True)
    #videocard
    Сериявидеокарты = models.CharField(max_length=20, null=True , blank=True)
    ПроизводительGPU = models.CharField(max_length=20, null=True , blank=True)
    Модельчипсета = models.CharField(max_length=20, null=True , blank=True)
    ЧастотавидеопроцессораOCMode = models.CharField(max_length=20, null=True , blank=True)
    Частотавидеопамяти = models.CharField(max_length=20, null=True , blank=True)
    Типвидеопамяти = models.CharField(max_length=20, null=True , blank=True)
    Объемвидеопамяти = models.CharField(max_length=20, null=True , blank=True)
    Разрядностьшинывидеопамяти = models.CharField(max_length=20, null=True , blank=True)
    Пропускнаяспособностьпамяти = models.CharField(max_length=20, null=True , blank=True)
    Количествоуниверсальныхпроцессоров = models.CharField(max_length=20, null=True , blank=True)
    ПоддерживаемыеAPI = models.CharField(max_length=20, null=True , blank=True)
    ПоддержкаMulti = models.CharField(max_length=20, null=True , blank=True)
    Интерфейсподключения = models.CharField(max_length=20, null=True , blank=True)
    Количествоподдерживаемыхмониторов = models.CharField(max_length=20, null=True , blank=True)
    Разъемы = models.CharField(max_length=20, null=True , blank=True)
    Максимальноеразрешение = models.CharField(max_length=20, null=True , blank=True)
    Охлаждение = models.CharField(max_length=20, null=True , blank=True)
    Разъемыпитания = models.CharField(max_length=20, null=True , blank=True)
    Минимальнаямощностьблокапитания = models.CharField(max_length=20, null=True , blank=True)
    Длинавидеокарты = models.CharField(max_length=20, null=True , blank=True)
    #processor
    Типпроцессора = models.CharField(max_length=20, null=True , blank=True)
    Сокет = models.CharField(max_length=20, null=True , blank=True)
    Количествоэнергоэффективныхядер = models.CharField(max_length=20, null=True , blank=True)
    Общееколичествоядер = models.CharField(max_length=20, null=True , blank=True)
    Количествопроизводительныхядер = models.CharField(max_length=20, null=True , blank=True)
    Количествопотоков = models.CharField(max_length=20, null=True , blank=True)
    Тактоваячастота = models.CharField(max_length=20, null=True , blank=True)
    Максимальнаятактоваячастота = models.CharField(max_length=20, null=True , blank=True)
    Тактоваячастотаэнергоэффективныхядер = models.CharField(max_length=20, null=True , blank=True)
    Максимальнаячастотаэнергоэффективныхядер = models.CharField(max_length=20, null=True , blank=True)
    Микроархитектура = models.CharField(max_length=20, null=True , blank=True)
    ОбъемкэшаL2 = models.CharField(max_length=20, null=True , blank=True)
    ОбъемкэшаL3 = models.CharField(max_length=20, null=True , blank=True)
    Типподдерживаемойпамяти = models.CharField(max_length=20, null=True , blank=True)
    Максимальныйобъемпамяти = models.CharField(max_length=20, null=True , blank=True)
    Техпроцесс = models.CharField(max_length=20, null=True , blank=True)
    Расчетнаямощность = models.CharField(max_length=20, null=True , blank=True)
    Максимальнаярасчетнаямощность = models.CharField(max_length=20, null=True , blank=True)
    Поддерживаемыетехнологии = models.CharField(max_length=20, null=True , blank=True)
    Поддерживаемыеинструкции = models.CharField(max_length=20, null=True , blank=True)
    Критическаятемпература = models.CharField(max_length=20, null=True , blank=True)
    Упаковка = models.CharField(max_length=20, null=True , blank=True)
    #mother b
    Поддержкамикроархитектурыпроцессора = models.CharField(max_length=20, null=True , blank=True)
    Чипсет = models.CharField(max_length=20, null=True , blank=True)
    Поддержкатехнологий = models.CharField(max_length=20, null=True , blank=True)
    Форм = models.CharField(max_length=20, null=True , blank=True)
    Количествослотовпамяти = models.CharField(max_length=20, null=True , blank=True)
    Поддерживаемыечастотыпамяти = models.CharField(max_length=20, null=True , blank=True)
    Внимание = models.CharField(max_length=20, null=True , blank=True)
    Maксимальныйобъемоперативнойпамяти = models.CharField(max_length=20, null=True , blank=True)
    КоличестворазъемовSATA3 = models.CharField(max_length=20, null=True , blank=True)
    Длинавидеокарты = models.CharField(max_length=20, null=True , blank=True)
    Длинавидеокарты = models.CharField(max_length=20, null=True , blank=True)
    Длинавидеокарты = models.CharField(max_length=20, null=True , blank=True)
    Длинавидеокарты = models.CharField(max_length=20, null=True , blank=True)
    Длинавидеокарты = models.CharField(max_length=20, null=True , blank=True)
    Длинавидеокарты = models.CharField(max_length=20, null=True , blank=True)
    Длинавидеокарты = models.CharField(max_length=20, null=True , blank=True)
    Длинавидеокарты = models.CharField(max_length=20, null=True , blank=True)
    Длинавидеокарты = models.CharField(max_length=20, null=True , blank=True)
    Длинавидеокарты = models.CharField(max_length=20, null=True , blank=True)




