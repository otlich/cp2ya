# cp2ya
Утилита для копирования файлов на yandex disk из командной строки linux на основе либы [YaDiskClient](https://github.com/TyVik/YaDiskClient).
Для установки требуемой библиотеки pip install YaDiskClient или easy_install YaDiskClient

#Использование
cp2ya /localFile /FileNameOnYandexDisk

# Конфигурация 
Имя пользователя и пароль от yandex необходимо указать в конфигурационном файле в домашнем каталоге пользователя ~/.cp2ya

# Формат конфига
[auth]

login = userName@yandex.ru

password = userPassword

