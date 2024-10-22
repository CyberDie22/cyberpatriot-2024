# (L1) Ensure 'dom.disable_window_move_resize' is set to 'Enabled'

## Description

The `dom.disable_window_move_resize` preference in Mozilla Firefox is a crucial security configuration that prevents malicious scripts from moving or resizing browser windows. When not properly configured, this can lead to potential security risks:

- **Steganography:** Attackers could obscure malicious activity by minimizing or hiding browser windows.
- **Deception:** Unexpected window movements could be used in social engineering attacks.
- **Unintended Interactions:** Conflicts may arise with other applications due to uncontrolled window movements.

This vulnerability is not a flaw in Firefox's code, but rather a configuration issue that needs to be addressed through proper Group Policy settings.

## Audit

To audit this setting:

### Windows:

1. Open the Group Policy Management Console.
2. Navigate to the following path:
   ```
   Computer Configuration\Policies\Administrative Templates\Mozilla\Firefox\Preferences (Deprecated)\dom.disable_window_move_resize
   ```
3. Verify that the setting is set to "Enabled".

Alternatively, check the registry:

1. Open the Registry Editor.
2. Navigate to:
   ```
   HKLM\SOFTWARE\Policies\Mozilla\Firefox\Preferences
   ```
3. Verify that the `dom.disable_window_move_resize` value exists and is set to `1` (DWORD).

### Linux:

Firefox on Linux typically doesn't use Group Policy. Instead, check the `user.js` or `prefs.js` file in the Firefox profile directory:

1. Locate the Firefox profile directory (usually in `~/.mozilla/firefox/`).
2. Open the `user.js` or `prefs.js` file in a text editor.
3. Look for the following line:
   ```
   user_pref("dom.disable_window_move_resize", true);
   ```
4. Ensure this line exists and is not commented out.

## Remediation

To remediate this issue:

### Windows:

1. Download and install the Firefox ADMX template from [Mozilla's GitHub repository](https://github.com/mozilla/policy-templates/releases).
2. Open the Group Policy Management Console.
3. Navigate to:
   ```
   Computer Configuration\Policies\Administrative Templates\Mozilla\Firefox\Preferences (Deprecated)\dom.disable_window_move_resize
   ```
4. Set the policy to "Enabled".
5. Run `gpupdate /force` to apply the changes.

### Linux:

1. Locate the Firefox profile directory (usually in `~/.mozilla/firefox/`).
2. Create or edit the `user.js` file in this directory.
3. Add or modify the following line:
   ```javascript
   user_pref("dom.disable_window_move_resize", true);
   ```
4. Save the file and restart Firefox.

For system-wide deployment on Linux, consider using a configuration management tool to distribute this setting across multiple machines.