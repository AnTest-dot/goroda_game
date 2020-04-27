import random


def more():
    print("Подходит. Отлично! Продолжаем.")
    # cities_towns.remove(gorod)
    print("Повторять слова нельзя.")


def not_match():
    print("Однако ваше название начинается не с той буквы.")


def game_function():
    cities_towns = ["Абаза", "Абакан", "Абдулино", "Абинск", "Агидель", "Агрыз",
                    "Адыгейск", "Азнакаево", "Азов", "Ак-Довурак", "Аксай",
                    "Аксубаево ", "Актюбинский ", "Алагир", "Алапаевск",
                    "Алатырь", "Алдан", "Алейск", "Александров", "Александровск",
                    "Александровск-Сахалинский", "Алексеевка", "Алексеевское ",
                    "Алексин", "Алзамай", "Али-Бердуковский", "Алтухово", "Алупка",
                    "Алушта", "Альметьевск", "Амурск", "Анадырь", "Анапа", "Ангарск",
                    "Андреаполь", "Анжеро-Судженск", "Анива", "Апастово ", "Апатиты",
                    "Апрелевка", "Апшеронск", "Арамиль", "Аргун", "Ардатов", "Ардон",
                    "Арзамас", "Аркадак", "Армавир", "Армянск", "Арсеньев", "Арск",
                    "Артём", "Артёмовск", "Артёмовский", "Архангельск", "Архонская",
                    "Асбест", "Асино", "Астрахань", "Аткарск", "Ахтубинск", "Ачинск",
                    "Аша", "Бабаево", "Бабушкин", "Бавлы", "Багратионовск", "Байкальск",
                    "Баймак", "Бакал", "Баксан", "Балабаново", "Балаково", "Балахна",
                    "Балашиха", "Балашов", "Балей", "Балтаси ", "Балтийск", "Барабинск",
                    "Барнаул", "Барыш", "Батайск", "Бахчисарай", "Башмаково ", "Бежаницы",
                    "Бежецк", "Беково ", "Белая Берёзка", "Белая Калитва", "Белая Холуница",
                    "Белгород", "Белебей", "Белёв", "Белинский", "Белово", "Белогорск",
                    "Белогорск", "Белозерск", "Белокуриха", "Беломорск", "Белорецк",
                    "Белореченск", "Белоусово", "Белоярский", "Белушья Губа", "Белые Берега",
                    "Белый", "Бердск", "Березник", "Березники", "Берёзовский", "Берёзовский",
                    "Беслан", "Бийск", "Бикин", "Билибино", "Биробиджан", "Бирск",
                    "Бирюсинск", "Бирюч", "Благовещенск", "Благовещенск", "Благодарный",
                    "Бобров", "Богатые Сабы ", "Богданович", "Богородицк", "Богородск",
                    "Боготол", "Богучар", "Бодайбо", "Бокситогорск", "Болгар", "Бологое",
                    "Болотное", "Болохово", "Болхов", "Большое Полпино", "Большой Камень",
                    "Бор", "Борзя", "Борисоглебск", "Боровичи", "Боровск", "Бородино",
                    "Братск", "Бронницы", "Брянск", "Бугульма", "Бугуруслан", "Будённовск",
                    "Бузулук", "Буинск", "Буй", "Буйнакск", "Бутурлиновка", "Бытошь",
                    "Валдай", "Валуйки", "Васильево ", "Велиж", "Великие Луки",
                    "Великий Новгород", "Великий Устюг", "Вельск", "Венёв", "Верещагино",
                    "Верея", "Верхнеднепровский ", "Верхнеуральск", "Верхний Тагил",
                    "Верхний Уфалей", "Верхняя Пышма", "Верхняя Салда", "Верхняя Тура",
                    "Верхозим ", "Верхотурье", "Верхоянск", "Весьегонск", "Ветлуга",
                    "Видное", "Вилюйск", "Вилючинск", "Вихоревка", "Вичуга", "Владивосток",
                    "Владикавказ", "Владимир", "Волгоград", "Волгодонск", "Волгореченск",
                    "Волжск", "Волжский", "Вологда", "Володарск", "Волоколамск", "Волосово",
                    "Волхов", "Волчанск", "Вольск", "Воркута", "Воронеж", "Ворсма",
                    "Воскресенск", "Воткинск", "Всеволожск", "Вуктыл", "Выборг",
                    "Выгоничи", "Выкса", "Высоковск", "Высоцк", "Вытегра", "Вычегодский",
                    "Вышков", "Вышний Волочёк", "Вяземский", "Вязники", "Вязьма",
                    "Вятские Поляны", "Гаврилов Посад", "Гаврилов-Ям", "Гагарин",
                    "Гаджиево", "Гай", "Галич", "Гаспра", "Гатчина", "Гвардейск",
                    "Гвардейское", "Гдов", "Геленджик", "Георгиевск", "Гизель", "Глазов",
                    "Голицыно", "Голынки ", "Горагорск ", "Горбатов", "Горно-Алтайск",
                    "Горнозаводск", "Горняк", "Городец", "Городище", "Городовиковск",
                    "Гороховец", "Горячий Ключ", "Грайворон", "Гремячинск", "Грозный",
                    "Грязи", "Грязовец", "Губаха", "Губкин", "Губкинский", "Гудермес",
                    "Гуково", "Гулькевичи", "Гурьевск", "Гурьевск", "Гусев", "Гусиноозёрск",
                    "Гусь-Хрустальный", "Давлеканово", "Дагестанские Огни", "Далматово",
                    "Дальнегорск", "Дальнереченск", "Данилов", "Данков", "Дегтярск",
                    "Дедовичи", "Дедовск", "Демидов", "Дербент", "Десногорск", "Джалиль ",
                    "Джанкой", "Дзержинск", "Дзержинский", "Дивногорск", "Дигора",
                    "Димитровград", "Дмитриев", "Дмитриевка", "Дмитров", "Дмитровск",
                    "Дно", "Добрянка", "Долгопрудный", "Долинск", "Домодедово", "Донецк",
                    "Донской", "Дорогобуж", "Дрезна", "Дубна", "Дубовка", "Дубровка",
                    "Дудинка", "Духовщина", "Дюртюли", "Дятьково", "Евлашево ", "Евпатория",
                    "Егорьевск", "Ейск", "Екатеринбург", "Елабуга", "Елец", "Елизово",
                    "Ельня", "Еманжелинск", "Емва", "Емца", "Енисейск", "Ермолино", "Ершов",
                    "Ессентуки", "Ефремов", "Железноводск", "Железногорск", "Железногорск",
                    "Железногорск-Илимский", "Жердевка", "Жигулёвск", "Жиздра", "Жирновск",
                    "Жуков", "Жуковка", "Жуковский", "Завитинск", "Заводоуковск", "Заводской",
                    "Заволжск", "Заволжье", "Задонск", "Заинск", "Закаменск", "Заозёрный",
                    "Заозёрск", "Западная Двина", "Заплюсье", "Заполярный", "Зарайск",
                    "Заречный", "Заречный", "Заринск", "Звенигово", "Звенигород", "Зверево",
                    "Зеленогорск", "Зеленоградск", "Зеленодольск", "Зеленокумск",
                    "Зеленчукская", "Земетчино ", "Зерноград", "Зея", "Зима", "Златоуст",
                    "Злынка", "Змеиногорск", "Змейская", "Знаменка", "Знаменск",
                    "Золотарёвка ", "Зубцов", "Зуевка", "Ивангород", "Иваново", "Ивантеевка",
                    "Ивдель", "Ивот", "Игарка", "Идрица", "Ижевск", "Избербаш", "Изобильный",
                    "Иланский", "Инжавино", "Инза", "Инкерман", "Иннополис", "Инсар",
                    "Инта", "Ипатово", "Ирбит", "Иркутск", "Исилькуль", "Искитим", "Исса ",
                    "Истра", "Ишим", "Ишимбай", "Йошкар-Ола", "Кадников", "Казань",
                    "Калач", "Калачинск", "Калач-На-Дону", "Калининград", "Калининск",
                    "Калтан", "Калуга", "Калязин", "Камбарка", "Камбилеевское", "Каменка",
                    "Каменка", "Каменногорск", "Каменск-Уральский", "Каменск-Шахтинский",
                    "Камень-На-Оби", "Камешково", "Камские Поляны ", "Камское Устье ",
                    "Камызяк", "Камышин", "Камышлов", "Канаш", "Кандалакша", "Канск",
                    "Карабаново", "Карабаш", "Карабаш ", "Карабулак", "Карасук", "Карачаевск",
                    "Карачев", "Каргат", "Каргополь", "Кардоникская", "Кардымово ", "Карпинск",
                    "Карталы", "Касимов", "Касли", "Каспийск", "Катав-Ивановск", "Катайск",
                    "Качканар", "Кашин", "Кашира", "Кедровый", "Кемерово", "Кемь", "Керчь",
                    "Кизел", "Кизилюрт", "Кизляр", "Кизляр", "Кимовск", "Кимры", "Кингисепп",
                    "Кинель", "Кинешма", "Киреевск", "Киренск", "Киржач", "Кириллов", "Кириши",
                    "Киров", "Киров", "Кировград", "Кирово-Чепецк", "Кировск", "Кировск",
                    "Кирс", "Кирсанов", "Киселёвск", "Кисловодск", "Клетня", "Климово", "Клин",
                    "Клинцы", "Княгинино", "Ковдор", "Ковров", "Ковылкино", "Когалым",
                    "Кодинск", "Козельск", "Козловка", "Козьмодемьянск", "Кокоревка", "Кола",
                    "Кологрив", "Коломна", "Колпашево", "Колышлей ", "Кольчугино", "Комаричи",
                    "Коммунар", "Комсомольск", "Комсомольск-На-Амуре", "Конаково", "Кондопога",
                    "Кондрово", "Коноша", "Константиновск", "Копейск", "Кораблино",
                    "Кореновск", "Коркино", "Королёв", "Короча", "Корсаков", "Коряжма",
                    "Костерёво", "Костомукша", "Кострома", "Котельники", "Котельниково",
                    "Котельнич", "Котлас", "Котово", "Котовск", "Кохма", "Красавино",
                    "Красная Гора", "Красная Горбатка ", "Красноармейск", "Красноармейск",
                    "Красновишерск", "Красногвардейское", "Красногородск", "Красногорск",
                    "Краснодар", "Краснозаводск", "Краснознаменск", "Краснознаменск",
                    "Краснокаменск", "Краснокамск", "Красноперекопск", "Краснослободск",
                    "Краснослободск", "Краснотурьинск", "Красноуральск", "Красноуфимск",
                    "Красноярск", "Красный ", "Красный Кут", "Красный Луч", "Красный Сулин",
                    "Красный Холм", "Кремёнки", "Кропоткин", "Крымск", "Кстово", "Кубинка",
                    "Кувандык", "Кувшиново", "Кудымкар", "Кузнецк", "Куйбышев",
                    "Куйбышевский Затон ", "Кукмор", "Кулебаки", "Кулой", "Кумертау",
                    "Кумыш", "Кунгур", "Кунья", "Купино", "Курган", "Курганинск",
                    "Курджиново", "Курильск", "Курлово", "Куровское", "Курск", "Куртамыш",
                    "Курчатов", "Куса", "Кушва", "Кызыл", "Кыштым", "Кяхта", "Лабинск",
                    "Лабытнанги", "Лагань", "Ладушкин", "Лаишево", "Лакинск", "Лангепас",
                    "Лахденпохья", "Лебедянь", "Лениногорск", "Ленинск", "Ленинск-Кузнецкий",
                    "Ленск", "Лермонтов", "Лесной", "Лесозаводск", "Лесосибирск", "Ливны",
                    "Ликино-Дулёво", "Липецк", "Липки", "Лиски", "Лихославль", "Лобня",
                    "Лодейное Поле", "Локня", "Локоть", "Лосино-Петровский", "Луга", "Луза",
                    "Луковская", "Лукоянов", "Лунино ", "Луховицы", "Лысково", "Лысьва",
                    "Лыткарино", "Льгов", "Любань", "Люберцы", "Любим", "Любохна", "Людиново",
                    "Лянтор", "Магадан", "Магас", "Магнитогорск", "Майкоп", "Майский",
                    "Майское", "Макаров", "Макарьев", "Макушино", "Малая Вишера", "Малгобек",
                    "Малмыж", "Малоархангельск", "Малошуйка", "Малоярославец", "Мамадыш",
                    "Мамоново", "Мантурово", "Мариинск", "Мариинский Посад", "Маркс",
                    "Махачкала", "Мглин", "Мегион", "Медвежьегорск", "Медногорск",
                    "Медногорский", "Медынь", "Межгорье", "Междуреченск", "Мезень", "Меленки",
                    "Мелеуз", "Менделеевск", "Мензелинск", "Мещовск", "Миасс", "Микунь",
                    "Миллерово", "Минеральные Воды", "Минусинск", "Миньяр", "Мирный",
                    "Мирный", "Михайлов", "Михайловка", "Михайловск", "Михайловск",
                    "Михайловское", "Мичуринск", "Могоча", "Можайск", "Можга", "Моздок",
                    "Мокшан ", "Монастырщина ", "Мончегорск", "Мордово", "Морозовск",
                    "Моршанск", "Мосальск", "Москва", "Муравленко", "Мураши", "Мурманск",
                    "Муром", "Мучкапский", "Мценск", "Мыски", "Мытищи", "Мышкин",
                    "Набережные Челны", "Навашино", "Навля", "Наволоки", "Надым",
                    "Назарово", "Назрань", "Называевск", "Нальчик", "Нариманов",
                    "Наро-Фоминск", "Нарткала", "Нарьян-Мар", "Находка", "Невель",
                    "Невельск", "Невинномысск", "Невьянск", "Нелидово", "Неман",
                    "Нерехта", "Нерчинск", "Нерюнгри", "Нестеров", "Нефтегорск",
                    "Нефтекамск", "Нефтекумск", "Нефтеюганск", "Нея", "Нижневартовск",
                    "Нижнекамск", "Нижнеудинск", "Нижние Вязовые ", "Нижние Серги",
                    "Нижний Ломов", "Нижний Новгород", "Нижний Тагил", "Нижняя Мактама ",
                    "Нижняя Салда", "Нижняя Тура", "Николаевск", "Николаевск-На-Амуре",
                    "Никольск", "Никольск", "Никольское", "Новая Ладога", "Новая Ляда",
                    "Новая Ляля", "Новоалександровск", "Новоалтайск", "Новоаннинский",
                    "Нововоронеж", "Новодвинск", "Новозыбков", "Новокубанск", "Новокузнецк",
                    "Новокуйбышевск", "Новомичуринск", "Новомосковск", "Новопавловск",
                    "Новопокровка", "Новоржев", "Новороссийск", "Новосибирск", "Новосиль",
                    "Новосокольники", "Новотроицк", "Новоузенск", "Новоульяновск",
                    "Новоуральск", "Новохопёрск", "Новочебоксарск", "Новочеркасск",
                    "Новошахтинск", "Новый Оскол", "Новый Уренгой", "Ногинск", "Ногир",
                    "Нолинск", "Норильск", "Ноябрьск", "Нурлат", "Нытва", "Нюрба", "Нягань",
                    "Нязепетровск", "Няндома", "Облучье", "Обнинск", "Обозерский", "Обоянь",
                    "Обь", "Одинцово", "Озёрный ", "Озёрск", "Озёрск", "Озёры", "Ойсхара ",
                    "Оксовский", "Октябрьск", "Октябрьский", "Октябрьский", "Октябрьское",
                    "Октябрьское", "Окуловка", "Олёкминск", "Оленегорск", "Олонец", "Омск",
                    "Омутнинск", "Онега", "Опочка", "Орёл", "Оренбург", "Орехово-Зуево",
                    "Орлов", "Орск", "Оса", "Осинники", "Осташков", "Остров", "Островной",
                    "Острогожск", "Отрадное", "Отрадный", "Оха", "Оханск", "Очёр", "Павлово",
                    "Павловск", "Павловский Посад", "Павлодольская", "Палкино", "Палласовка",
                    "Партизанск", "Пачелма ", "Певек", "Пенза", "Первомайск", "Первомайский",
                    "Первомайское", "Первоуральск", "Перевоз", "Пересвет",
                    "Переславль-Залесский", "Пермь", "Пестово", "Петров Вал", "Петровск",
                    "Петровск-Забайкальский", "Петрозаводск", "Петропавловск-Камчатский",
                    "Петухово", "Петушки", "Печора", "Печоры", "Пикалёво", "Пионерский",
                    "Питкяранта", "Плавск", "Пласт", "Плёс", "Плесецк", "Плюсса", "Поворино",
                    "Погар", "Подольск", "Подпорожье", "Покачи", "Покров", "Покровск",
                    "Полевской", "Полесск", "Полысаево", "Полярные Зори", "Полярный",
                    "Поронайск", "Порхов", "Похвистнево", "Почеп", "Починок", "Пошехонье",
                    "Правдинск", "Преградная", "Пржевальское ", "Приводино", "Приволжск",
                    "Приморск", "Приморск", "Приморский", "Приморско-Ахтарск", "Приозерск",
                    "Прокопьевск", "Пролетарск", "Протвино", "Прохладный", "Псков", "Псыж",
                    "Пугачёв", "Пудож", "Пуксоозеро", "Пустошка", "Пучеж", "Пушкино",
                    "Пушкинские Горы", "Пущино", "Пыталово", "Пыть-Ях", "Пятигорск",
                    "Радица-Крыловка", "Радужный", "Радужный", "Райчихинск", "Рамасуха",
                    "Раменское", "Рассказово", "Ревда", "Реж", "Реутов", "Ржакса", "Ржев",
                    "Рогнедино", "Родники", "Рославль", "Россошь", "Ростов", "Ростов-На-Дону",
                    "Рошаль", "Ртищево", "Рубцовск", "Рудня", "Руза", "Рузаевка", "Рыбинск",
                    "Рыбная Слобода ", "Рыбное", "Рыльск", "Ряжск", "Рязань", "Савинский",
                    "Саки", "Салават", "Салаир", "Салехард", "Сальск", "Самара", "Самодед",
                    "Санкт-Петербург", "Саранск", "Сарапул", "Саратов", "Саров", "Сасово",
                    "Сатка", "Сафоново", "Саяногорск", "Саянск", "Светлогорск", "Светлоград",
                    "Светлый", "Светогорск", "Свирск", "Свободный", "Себеж", "Севастополь",
                    "Северобайкальск", "Северодвинск", "Северо-Курильск", "Североморск",
                    "Североонежск", "Североуральск", "Северск", "Севск", "Сегежа", "Сельцо",
                    "Семёнов", "Семикаракорск", "Семилуки", "Сенгилей", "Серафимович",
                    "Сергач", "Сергиев Посад ", "Сердобск", "Серов", "Серпухов", "Сертолово",
                    "Сибай", "Сим", "Симферополь", "Сковородино", "Скопин", "Славгород",
                    "Славск", "Славянск-На-Кубани", "Сланцы", "Слободской", "Слюдянка",
                    "Смоленск", "Снежинск", "Снежногорск", "Собинка", "Советск", "Советск",
                    "Советск", "Советская Гавань", "Советский", "Советский", "Сокол",
                    "Солигалич", "Соликамск", "Солнечногорск", "Сольвычегодск", "Соль-Илецк",
                    "Сольцы", "Сорочинск", "Сорск", "Сортавала", "Сосенский", "Сосновка",
                    "Сосновка", "Сосновоборск", "Сосновоборск ", "Сосновый Бор",
                    "Сосновый Бор", "Сосногорск", "Сочи", "Спас-Деменск", "Спас-Клепики",
                    "Спасск", "Спасск-Дальний", "Спасск-Рязанский", "Среднеколымск",
                    "Среднеуральск", "Сретенск", "Ставрополь", "Старая Купавна",
                    "Старая Русса", "Старица", "Стародуб", "Старый Крым", "Старый Оскол",
                    "Старь", "Стерлитамак", "Сторожевая", "Стрежевой", "Строитель",
                    "Струги Красные", "Струнино", "Ступино", "Суворов", "Судак", "Суджа",
                    "Судогда", "Суздаль", "Суземка", "Сунжа", "Сунжа", "Суоярви", "Сура ",
                    "Сураж", "Сургут", "Суровикино", "Сурск", "Сусуман", "Сухиничи",
                    "Сухой Лог", "Сызрань", "Сыктывкар", "Сысерть", "Сычёвка", "Сясьстрой",
                    "Тавда", "Таганрог", "Тайга", "Тайшет", "Талдом", "Талица", "Тамала ",
                    "Тамбов", "Тара", "Тарко-Сале", "Таруса", "Татарск", "Таштагол", "Тверь",
                    "Теберда", "Тейково", "Темников", "Темрюк", "Тенишево ", "Терезе",
                    "Терек", "Тетюши", "Тимашёвск", "Тихвин", "Тихорецк", "Тлюстенхабль ",
                    "Тобольск", "Тогучин", "Токарёвка", "Тольятти", "Томари", "Томмот",
                    "Томск", "Топки", "Торжок", "Торопец", "Тосно", "Тотьма", "Трёхгорный",
                    "Троицк", "Трубчевск", "Туапсе", "Туймазы", "Тула", "Тулун", "Туран",
                    "Туринск", "Тутаев", "Тында", "Тырныауз", "Тюкалинск", "Тюмень",
                    "Уварово", "Углегорск", "Углич", "Удачный", "Удомля", "Ужур", "Узловая",
                    "Улан-Удэ", "Ульяновск", "Умёт", "Унеча", "Урай", "Урдома", "Урень",
                    "Уржум", "Урус-Мартан", "Уруссу ", "Урюпинск", "Усвяты", "Усинск",
                    "Усмань", "Усолье", "Усолье-Сибирское", "Уссурийск", "Усть-Абакан ",
                    "Усть-Джегута", "Усть-Илимск", "Усть-Катав", "Усть-Кут", "Усть-Лабинск",
                    "Устюжна", "Уфа", "Ухта", "Учалы", "Учкекен", "Уяр", "Фатеж", "Феодосия",
                    "Фокино", "Фокино", "Фролово", "Фрязино", "Фурманов", "Хабаровск",
                    "Хабез", "Хадыженск", "Ханты-Мансийск", "Харабали", "Харовск", "Хасавюрт",
                    "Хвалынск", "Хилок", "Химки", "Хиславичи ", "Холм", "Холм-Жирковский ",
                    "Холмск", "Хотьково", "Цивильск", "Цимлянск", "Циолковский", "Чаадаевка ",
                    "Чадан", "Чайковский", "Чапаевск", "Чапаевское", "Чаплыгин", "Чебаркуль",
                    "Чебоксары", "Чегем", "Чекалин", "Челябинск", "Чердынь", "Черемхово",
                    "Черепаново", "Череповец", "Черкесск", "Чермен", "Чёрмоз", "Черноголовка",
                    'Черногорск', "Черноморское", "Чернушка", "Черняховск", "Чехов", "Чикола",
                    "Чири-Юрт ", "Чистополь", "Чита", "Чкаловск", "Чудово", "Чулым",
                    "Чусовой", "Чухлома", "Шагонар", "Шадринск", "Шали", "Шарыпово", "Шарья",
                    "Шатура", "Шахты", "Шахунья", "Шацк", "Шебекино", "Шелехов", "Шемышейка ",
                    "Шенкурск", "Шилка", "Шимановск", "Шипицыно", "Шиханы", "Шлиссельбург",
                    "Шумерля", "Шумиха", "Шумячи ", "Шуя", "Щёкино", "Щёлкино", "Щёлково",
                    "Щигры", "Щучье", "Электрогорск", "Электросталь", "Электроугли", "Элиста",
                    "Эльхотово", "Энгельс", "Энем ", "Эртиль", "Югорск", "Южа",
                    "Южно-Сахалинск", "Южно-Сухокумск", "Южноуральск", "Юрга", "Юрьевец",
                    "Юрьев-Польский", "Юрюзань", "Юхнов", "Яблоновский ", "Ядрин", "Якутск",
                    "Ялта", "Ялуторовск", "Янаул", "Яранск", "Яровое", "Ярославль", "Ярцево",
                    'Ясногорск', "Ясный", "Яхрома"]

    while True:

        city_town = random.choice(cities_towns)
        your_try = 0
        gamer_see = city_town
        print("\n" + gamer_see)
        # cities_towns.remove(city_town)
        print("Повторять слова нельзя.")

        while True:

            gorod = input(
                "Введите российский город, название города должно начинаться с последней буквы предыдущего слова "
                "(если город кончается на Ы или Ь,введите город на предпоследнюю букву): ")

            if gorod.isascii():
                print("Название города должно быть написано кириллицей.")
                continue

            else:
                print("Название на русском.")

                if gorod in cities_towns:
                    print("Город найден.")
                    gorod = gorod.lower()

                    if list(gamer_see[-1]) == "ь" or list(gamer_see[-1]) == "ы":
                        if list(gamer_see[-2]) == list(gorod[0]):
                            more()

                            while True:
                                gamer_see = random.choice(cities_towns)
                                gamer_see2 = gamer_see.lower()

                                if list(gamer_see2[0]) != list(gorod[-1]) or list(gamer_see2[-1]) == "ь" or list(
                                        gamer_see2[-1] == "ы"):
                                    print("Ищем слово...")
                                    continue
                                else:
                                    print("\n" + gamer_see)
                                    break

                        else:
                            not_match()
                            continue

                    else:
                        if list(gamer_see[-1]) == list(gorod[0]):
                            more()
                            while True:
                                gamer_see = random.choice(cities_towns)
                                gamer_see2 = gamer_see.lower()

                                if list(gorod[-1]) == "ь" or list(gorod[-1]) == "ы":

                                    if list(gamer_see2[0]) != list(gorod[-2]):
                                        print("Ищем слово...")
                                        continue

                                    else:
                                        print("\n" + gamer_see)
                                        break
                                else:
                                    if list(gamer_see2[0]) != list(gorod[-1]):
                                        print("Ищем слово...")
                                        continue

                                    else:
                                        print("\n" + gamer_see)
                                        break
                        else:
                            not_match()
                            continue
                else:
                    print("Такого города в списке нет. Попробуйте ещё.")
                    your_try += 1
                    ostalos = 5 - your_try
                    print("Попытка №" + str(your_try) + ". Осталось " + str(ostalos) + " попыток.")
                    if your_try == 5:
                        print("Попытки кончились, вы проиграли. Новая игра.")
                        game_function()

                    continue

game_function()
