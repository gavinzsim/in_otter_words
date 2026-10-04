Add-Type -AssemblyName System.Drawing

$target = Join-Path $PSScriptRoot 'game\gui\otter'
New-Item -ItemType Directory -Force -Path $target | Out-Null

function New-RoundedImage($name, $width, $height, $radius, $fill, $outline, $stroke) {
    $bitmap = New-Object System.Drawing.Bitmap($width, $height)
    $bitmap.SetResolution(96, 96)
    $graphics = [System.Drawing.Graphics]::FromImage($bitmap)
    $graphics.SmoothingMode = [System.Drawing.Drawing2D.SmoothingMode]::AntiAlias
    $graphics.Clear([System.Drawing.Color]::Transparent)
    $rect = New-Object System.Drawing.RectangleF(($stroke / 2), ($stroke / 2), ($width - $stroke), ($height - $stroke))
    $diameter = $radius * 2
    $path = New-Object System.Drawing.Drawing2D.GraphicsPath
    $path.AddArc($rect.Left, $rect.Top, $diameter, $diameter, 180, 90)
    $path.AddArc(($rect.Right - $diameter), $rect.Top, $diameter, $diameter, 270, 90)
    $path.AddArc(($rect.Right - $diameter), ($rect.Bottom - $diameter), $diameter, $diameter, 0, 90)
    $path.AddArc($rect.Left, ($rect.Bottom - $diameter), $diameter, $diameter, 90, 90)
    $path.CloseFigure()
    $brush = New-Object System.Drawing.SolidBrush($fill)
    $graphics.FillPath($brush, $path)
    if ($stroke -gt 0) {
        $pen = New-Object System.Drawing.Pen($outline, $stroke)
        $graphics.DrawPath($pen, $path)
        $pen.Dispose()
    }
    $bitmap.Save((Join-Path $target $name), [System.Drawing.Imaging.ImageFormat]::Png)
    $brush.Dispose()
    $path.Dispose()
    $graphics.Dispose()
    $bitmap.Dispose()
}

$cream = [System.Drawing.Color]::FromArgb(242, 250, 246, 228)
$paper = [System.Drawing.Color]::FromArgb(250, 255, 251, 237)
$teal = [System.Drawing.Color]::FromArgb(237, 29, 82, 74)
$tealHover = [System.Drawing.Color]::FromArgb(246, 39, 111, 100)
$line = [System.Drawing.Color]::FromArgb(215, 160, 192, 159)
$leaf = [System.Drawing.Color]::FromArgb(240, 183, 211, 171)
$clear = [System.Drawing.Color]::Transparent

New-RoundedImage 'menu_panel.png' 128 128 28 ([System.Drawing.Color]::FromArgb(236, 24, 68, 63)) ([System.Drawing.Color]::FromArgb(200, 218, 233, 205)) 2
New-RoundedImage 'content_panel.png' 128 128 28 $paper $line 2
New-RoundedImage 'dialogue_panel.png' 128 128 28 ([System.Drawing.Color]::FromArgb(238, 252, 250, 235)) ([System.Drawing.Color]::FromArgb(235, 122, 165, 145)) 3
New-RoundedImage 'name_panel.png' 128 128 28 $teal ([System.Drawing.Color]::FromArgb(245, 223, 235, 207)) 2
New-RoundedImage 'button_idle.png' 128 128 26 $cream $line 3
New-RoundedImage 'button_hover.png' 128 128 26 $leaf ([System.Drawing.Color]::FromArgb(255, 86, 138, 113)) 3
New-RoundedImage 'button_selected.png' 128 128 26 ([System.Drawing.Color]::FromArgb(255, 209, 228, 194)) ([System.Drawing.Color]::FromArgb(255, 67, 121, 96)) 3
New-RoundedImage 'menu_button_idle.png' 128 128 26 ([System.Drawing.Color]::FromArgb(235, 245, 248, 227)) ([System.Drawing.Color]::FromArgb(210, 196, 222, 188)) 3
New-RoundedImage 'menu_button_hover.png' 128 128 26 ([System.Drawing.Color]::FromArgb(255, 255, 251, 232)) ([System.Drawing.Color]::FromArgb(255, 149, 192, 156)) 4
New-RoundedImage 'slot_idle.png' 128 128 25 $paper $line 3
New-RoundedImage 'slot_hover.png' 128 128 25 ([System.Drawing.Color]::FromArgb(255, 240, 250, 226)) ([System.Drawing.Color]::FromArgb(255, 65, 128, 106)) 5
New-RoundedImage 'quick_idle.png' 128 128 22 ([System.Drawing.Color]::FromArgb(190, 28, 67, 62)) $clear 0
New-RoundedImage 'quick_hover.png' 128 128 22 $tealHover $clear 0
New-RoundedImage 'bar_empty.png' 128 32 15 ([System.Drawing.Color]::FromArgb(255, 203, 219, 201)) $clear 0
New-RoundedImage 'bar_filled.png' 128 32 15 ([System.Drawing.Color]::FromArgb(255, 62, 134, 119)) $clear 0
New-RoundedImage 'bar_thumb.png' 40 40 19 ([System.Drawing.Color]::FromArgb(255, 248, 246, 223)) ([System.Drawing.Color]::FromArgb(255, 55, 114, 100)) 3
