# (L2) Ensure 'network.IDN_show_punycode' is set to 'Enabled'

## Description

This vulnerability relates to a configuration setting in Mozilla Firefox that determines how Internationalized Domain Names (IDNs) are displayed in the browser. The setting `network.IDN_show_punycode` controls whether IDNs are rendered as their Unicode representation or their Punycode equivalents.

When this setting is disabled, IDNs are displayed using their Unicode representation, which can potentially increase the risk of users falling victim to phishing attacks. Malicious actors could create domain names that appear visually similar to legitimate domains, making it harder for users to distinguish between genuine and spoofed websites.

The recommended state for this setting is: Enabled.

Enabling this setting ensures that IDNs are displayed in Punycode format, making it easier for users to identify potential spoofing attempts and reducing the risk of accessing malicious websites.

## Audit

To audit this setting, follow these steps:

1. Open the Group Policy Management Console (GPMC) on a domain controller or a system with the Group Policy Management tools installed.

2. Navigate to the following path:
   Computer Configuration\Policies\Administrative Templates\Mozilla\Firefox\Preferences (Deprecated)\network.IDN_show_punycode

3. Verify that the setting is configured as "Enabled".

Alternatively, you can check the registry:

1. Open the Registry Editor (regedit.exe).

2. Navigate to the following registry key:
   HKLM\SOFTWARE\Policies\Mozilla\Firefox\Preferences

3. Verify that the "network.IDN_show_punycode" value exists and is set to a REG_DWORD value of 1.

Note: The Group Policy template for Firefox (firefox.admx/adml) may need to be installed to access these settings.

## Remediation

### Windows:

To remediate this issue on Windows systems:

1. Download the Firefox Group Policy template (firefox.admx/adml) from:
   https://github.com/mozilla/policy-templates/releases

2. Copy the downloaded .admx file to `C:\Windows\PolicyDefinitions\` and the .adml file to the appropriate language subdirectory (e.g., `C:\Windows\PolicyDefinitions\en-US\`).

3. Open the Group Policy Management Console (GPMC).

4. Navigate to the policy you want to modify.

5. Go to: Computer Configuration\Policies\Administrative Templates\Mozilla\Firefox\Preferences (Deprecated)\network.IDN_show_punycode

6. Set the policy to "Enabled".

7. Apply the Group Policy changes.

### Linux:

For Linux systems, Firefox typically doesn't use Group Policy. Instead, you can configure this setting directly in Firefox:

1. Open Firefox.

2. In the address bar, type `about:config` and press Enter.

3. Accept the warning message if prompted.

4. Search for `network.IDN_show_punycode`.

5. Set the value to `true` by double-clicking on it.

Alternatively, you can create or modify the `user.js` file in the Firefox profile directory:

1. Locate the Firefox profile directory (typically in `~/.mozilla/firefox/`).

2. Create or edit the `user.js` file in the profile directory.

3. Add or modify the following line:
   ```
   user_pref("network.IDN_show_punycode", true);
   ```

4. Save the file and restart Firefox.

For system-wide configuration on Linux, consider using a configuration management tool to deploy these settings across multiple systems.