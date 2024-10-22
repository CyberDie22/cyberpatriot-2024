# (L1) Ensure 'extensions.blocklist.enabled' is set to 'Enabled'

## Description

The `extensions.blocklist.enabled` setting in Mozilla Firefox controls whether the browser retrieves a list of blocked applications from a server. This feature is crucial for preventing the installation of known malicious or potentially unwanted extensions. 

When enabled, Firefox checks this server-provided list before installing extensions, adding an extra layer of security to the browsing experience. The recommended and default state for this setting is **Enabled**.

It's important to note that this is not a vulnerability in the traditional sense, but rather a configuration best practice. Ensuring this setting is enabled helps maintain the intended security posture of the Firefox browser.

## Audit

To verify that the `extensions.blocklist.enabled` setting is correctly configured:

### Windows:

1. Open the Registry Editor (regedit.exe)
2. Navigate to the following key:
   ```
   HKLM\SOFTWARE\Policies\Mozilla\Firefox\Preferences
   ```
3. Look for the `extensions.blocklist.enabled` value
4. Confirm that it is set to `1` (REG_DWORD)

### Linux:

Firefox on Linux typically uses a different configuration method. You can check the setting by:

1. Open Firefox
2. In the address bar, type `about:config`
3. Search for `extensions.blocklist.enabled`
4. Verify that the value is set to `true`

## Remediation

To set the recommended configuration:

### Windows:

1. Open the Group Policy Management Console
2. Navigate to: Computer Configuration > Policies > Administrative Templates > Mozilla > Firefox > Preferences (Deprecated)
3. Find the setting "extensions.blocklist.enabled"
4. Set it to "Enabled"

Note: If the policy path doesn't exist, you may need to download and install the Firefox Group Policy template (firefox.admx/adml) from the Mozilla website.

Alternatively, you can set the registry value directly:

1. Open Registry Editor (regedit.exe)
2. Navigate to:
   ```
   HKLM\SOFTWARE\Policies\Mozilla\Firefox\Preferences
   ```
3. Create a new DWORD (32-bit) value named `extensions.blocklist.enabled`
4. Set its value to `1`

### Linux:

1. Locate your Firefox configuration file (usually in `~/.mozilla/firefox/<profile>/prefs.js`)
2. Add or modify the following line:
   ```
   user_pref("extensions.blocklist.enabled", true);
   ```
3. Save the file and restart Firefox

For system-wide configuration on Linux:

1. Create or edit `/etc/firefox/syspref.js`
2. Add the following line:
   ```
   pref("extensions.blocklist.enabled", true);
   ```
3. Save the file and restart Firefox on all affected systems

Remember to test these changes in a controlled environment before applying them widely to ensure they don't cause any unforeseen issues with your specific Firefox deployment.