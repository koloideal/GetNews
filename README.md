# GetNews

**GetNews** - это бот на Python, который мониторит новостной портал и скидывает пользователям новости при их выходе.

## Требования
- Учетная запись Telegram с полученными API-ключами (API_ID, API_HASH)
- Установленные зависимости, указанные в файле requirements.txt 
```
pip install -r requirements.txt
```

## Установка и настройка
- Склонируйте репозиторий
- Перед запуском бота создайте папку внутри репозитория с навзванием `secret_data`, в неё создайте файл `config.ini` с ключами и токенами
- config.ini должен иметь следующий вид:
```
[Telegram]
api_id = API_ID
api_hash = API_HASH
bot_token = BOT_TOKEN
creator_id = CREATOR_ID
```
- где api_id и api_hash - ваши Telegram API ключи(более подробная информация в интернете), bot_token - ваш идентификационный токен бота, creator_id - ваш id(не юзернейм) в Telegram
- установить зависмости консольной командой:
```
pip install -r requirements.txt
```

## Особенности использования
- Основной функционал бота заключается в автоматической отправке выходящих на портале новостей юзерам бота:
  
  1. Первоначальная настройка
    - После ввода команды /start ввести /config
    - Включить рассылку нажатием на соответствующую кнопку
    - При желании нажать на вторую кнопку и выполнить действия за выключенными тегами
    - Выключенные теги - теги, новости с которыми вам не будут приходить<br><br>


**Бот находится на стадии альфа-теста, поэтому баги и ошибки вполне вероятны и ожидаемы, в случае нахождения такого просьба скинуть скрины переписки с ботом в Telegram - <a href="https://t.me/kolo_id">@kolo_id<a>**


**Примечание:** Использование данного бота может быть ограничено правилами и политикой Telegram. Пожалуйста, убедитесь, что соблюдаете все правила Telegram при использовании этого бота.

