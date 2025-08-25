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
├── .gitignore
├── base_example.conf
├── base.conf
├── domains.txt
├── generate-conf.ps1
├── generate-conf.py
├── ReadMe.md
└── output.conf
```

6. Установите в клиенте WireGuard конфигурацию `output.conf`.

---

#### Вы потрясающий!  
 ![You are breathtaking](https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExa2VtZTZranp1OTlid2U4ZjVzcHZsYjJ2Ynl0aGg0bmhvOXI4bTJsZSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/V1dH38rUl9yX7xU8nh/giphy.gif)


