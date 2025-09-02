if (!([Security.Principal.WindowsPrincipal][Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole] "Administrator")) { Start-Process powershell.exe "-NoProfile -ExecutionPolicy Bypass -File `"$PSCommandPath`"" -Verb RunAs; exit }

# Список доменов
$domainList = Get-Content ".\domains.txt"
$ipList = @()

# Резолвим IP
foreach ($domain in $domainList) {
    try {
        $ips = [System.Net.Dns]::GetHostAddresses($domain) | Where-Object { $_.AddressFamily -eq 'InterNetwork' }
        foreach ($ip in $ips) {
            $ipList += "$($ip.IPAddressToString)/32"
        }
    } catch {
        Write-Warning "Не удалось резолвить $domain"
    }
}

# Склеим IP в одну строку
$allowedIPs = $ipList -join ", "

# Подставляем в base.conf
(Get-Content ".\base.conf") -replace 'AllowedIPs\s*=\s*.*', "AllowedIPs = $allowedIPs" |
    Set-Content ".\output.conf"

Write-Host "`n✅ Генерация завершена. AllowedIPs:"
$ipList | ForEach-Object { Write-Host " → $_" }

# Имя интерфейса в WireGuard (например, wg0)
$interfaceName = "output"

# Путь к файлу конфигурации в текущей папке скрипта
$configPath = Join-Path $PSScriptRoot "output.conf"

# Выключить интерфейс
& "C:\Program Files\WireGuard\wireguard.exe" /uninstalltunnelservice $interfaceName

# Установить заново с новым конфигом
& "C:\Program Files\WireGuard\wireguard.exe" /installtunnelservice  $configPath