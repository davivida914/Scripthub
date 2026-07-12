#!/usr/bin/env python3
import re

with open('/home/daytona/codebase/menu2.lua.txt', 'rb') as f:
    content = f.read()

# Check line endings
if b'\r\n' in content:
    nl = b'\r\n'
elif b'\n' in content:
    nl = b'\n'
else:
    nl = b'\n'

text = content.decode('utf-8', errors='replace')

# Find and replace the CheckBox function
old_checkbox = """function CheckBox(name, xx, yy, _, bool)
    local x,y = GetNuiCursorPosition()
    local x_res, y_res = GetActiveScreenResolution()
    local xx2 = xx-0.012
    local yy2 = yy+0.0020
    TxtCheckBox(name, xx2 + 0.003, yy2 - 0.0040, 0.30, 0, false, 255, 255, 255)

    if bool then
        DrawSprite(menu.txtnames.toggleon, menu.txtnames.toggleon, xx2-0.010, yy2, 0.020, 0.020, 0.0, 255, 255, 255, 255)
    else
        DrawSprite(menu.txtnames.toggleoff, menu.txtnames.toggleoff, xx2-0.010, yy2, 0.020, 0.020, 0.0, 255, 255, 255, 255)
    end

    if( (x / x_res) + 0.035 >= xx and (x / x_res) - 0.035 <= xx and (y / y_res) + 0.012 >= yy and (y / y_res) - 0.012 <= yy) and IsDisabledControlJustReleased(0, 92) then 
        return true
    end
    return false
end"""

new_checkbox = """function CheckBox(name, xx, yy, _, bool)
    local x,y = GetNuiCursorPosition()
    local x_res, y_res = GetActiveScreenResolution()
    local xx2 = xx-0.012
    local yy2 = yy+0.0020
    TxtCheckBox(name, xx2 + 0.003, yy2 - 0.0040, 0.30, 0, false, 255, 255, 255)

    -- Quadrado amarelo
    local cbX = xx2-0.010
    local cbY = yy2
    local cbW = 0.018
    local cbH = 0.018
    if bool then
        DrawRectangle(cbX, cbY, cbW, cbH, 255, 255, 0, 255)
        DrawRectangle(cbX, cbY, cbW-0.006, cbH-0.006, 255, 255, 255, 255)
    else
        DrawRectangle(cbX, cbY, cbW, cbH, 50, 50, 50, 255)
        DrawRectangle(cbX, cbY, cbW-0.004, cbH-0.004, 0, 0, 0, 200)
    end

    if( (x / x_res) + 0.035 >= xx and (x / x_res) - 0.035 <= xx and (y / y_res) + 0.012 >= yy and (y / y_res) - 0.012 <= yy) and IsDisabledControlJustReleased(0, 92) then 
        return true
    end
    return false
end"""

# Normalize line endings for matching
old_normalized = old_checkbox.replace('\r\n', '\n').replace('\n', nl.decode())
new_normalized = new_checkbox.replace('\r\n', '\n').replace('\n', nl.decode())

if old_normalized in text:
    text = text.replace(old_normalized, new_normalized)
    with open('/home/daytona/codebase/menu2.lua.txt', 'wb') as f:
        f.write(text.encode('utf-8'))
    print("SUCCESS: CheckBox function replaced!")
else:
    print("FAILED: Could not find the CheckBox function text")
    # Debug: find what's different
    print(f"Looking for pattern length: {len(old_normalized)}")
    # Try to find it with different line endings
    alt_old = old_checkbox.replace('\r\n', '\n').replace('\n', '\n')
    if alt_old in text:
        print("Found with \\n endings!")
    alt_old2 = old_checkbox.replace('\r\n', '\n').replace('\n', '\r\n')
    if alt_old2 in text:
        print("Found with \\r\\n endings!")
