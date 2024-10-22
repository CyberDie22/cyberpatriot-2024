# (L1) Ensure 'Do not allow preferences to be changed' is set to 'Enabled'

## Description

This policy setting configures whether the Firefox pop-up blocker settings can be changed by the user. The recommended state for this setting is: Enabled.

The vulnerability (more accurately, control weakness) concerns the enforced configuration of Firefox's pop-up blocker. If users can disable or modify the pop-up blocker settings, they could be exposed to malicious pop-up windows. These windows might be used for phishing, drive-by downloads, or other malicious activities, potentially leading to data breaches, malware infections, or financial losses.

The policy relies on the `HKLM\SOFTWARE\Policies\Mozilla\Firefox\PopupBlocking:Locked` registry key being set to 1. This key, by design, locks down a key configuration allowing user interaction with the popup blocker settings. If that key is missing or set to 0 (or if the policy isn't configured at all), users can access and change these settings.

## Audit

### Windows

1. Open the Group Policy Management Console (gpmc.msc).
2. Navigate to the following UI path:
   ```
   Computer Configuration\Policies\Administrative Templates\Mozilla\Firefox\Popups\Do not allow preferences to be changed
   ```
3. Verify that the setting is set to "Enabled".

Alternatively, you can check the registry:

1. Open the Registry Editor (regedit.exe).
2. Navigate to the following key:
   ```
   HKLM\SOFTWARE\Policies\Mozilla\Firefox\PopupBlocking
   ```
3. Verify that the "Locked" value exists and is set to 1 (REG_DWORD).

### Linux

Firefox on Linux typically doesn't use Group Policy. However, you can check the user preferences:

1. Open the Firefox profile directory (usually located in `~/.mozilla/firefox/`).
2. Open the `user.js` file in a text editor.
3. Look for a line containing `user_pref("browser.popup_blocker.enabled", true);`.
4. Ensure this line exists and is not commented out.

## Remediation

### Windows

To establish the recommended configuration via Group Policy:

1. Ensure you have the Firefox ADMX/ADML template files. If not, download them from the official Mozilla website.
2. Open the Group Policy Management Console (gpmc.msc).
3. Navigate to the following UI path:
   ```
   Computer Configuration\Policies\Administrative Templates\Mozilla\Firefox\Popups\Do not allow preferences to be changed
   ```
4. Set the policy to "Enabled".

If you need to set this manually in the registry:

1. Open the Registry Editor (regedit.exe).
2. Navigate to the following key (create it if it doesn't exist):
   ```
   HKLM\SOFTWARE\Policies\Mozilla\Firefox\PopupBlocking
   ```
3. Create a new DWORD value named "Locked" and set it to 1.

### Linux

On Linux systems, you can enforce this setting by creating or modifying the `mozilla.cfg` file:

1. Create or edit the file `/usr/lib/firefox/mozilla.cfg`.
2. Add the following line:
   ```javascript
   lockPref("browser.popup_blocker.enabled", true);
   ```
3. Save the file and restart Firefox.

Note: Ensure that the `mozilla.cfg` file is readable by all users but writable only by root.