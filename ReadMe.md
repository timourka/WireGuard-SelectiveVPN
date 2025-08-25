# WireGuard-SelectiveVPN

Простой способ создать селективную конфигурацию WireGuard.

---

## Быстрый старт

1. Установите WireGuard и получите конфигурационный файл от вашего сервера.

2. Скопируйте файл конфигурации в корень репозитория и назовите его:

```
base.conf
```

3. Запустите любой из скриптов генерации:

```
generate-conf.ps1, generate-conf.py
```

4. После выполнения скрипта появится файл:

```
output.conf
```

5. Итоговая структура корня репозитория будет примерно такой:

```
WireGuard-SelectiveVPN/
├── base.conf
├── domains.txt
├── generate-conf.ps1
├── generate-conf.py
└── output.conf
```

6. Установите в клиенте WireGuard конфигурацию `output.conf`.

---

Вы потрясающий! ![You are breathtaking](https://tenor.com/ru/view/willem-dafoe-willem-keanu-reeves-youre-breathtaking-breathtaking-gif-23688540)


