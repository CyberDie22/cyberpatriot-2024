# (L1) Ensure 'browser.search.update' is set to 'Enabled'

## Description

The `browser.search.update` policy setting in Firefox controls whether installed search providers are automatically updated. The recommended and default state for this setting is "Enabled". However, the vulnerability lies in the potential for misconfiguration of this policy.

If this setting is not properly configured or enforced, it can lead to:

- Compromised security due to outdated search providers lacking the latest security patches
- Reduced functionality as search providers become outdated or incompatible with new Firefox features
- Lack of observability across managed devices, masking potential risks

This vulnerability applies to systems using Group Policy to manage Firefox installations where the `browser.search.update` setting isn't automatically managed.

## Audit

To audit this setting:

### Windows:

1. Open the Group Policy Management Console
2. Navigate to the following UI path:
   ```
   Computer Configuration\Policies\Administrative Templates\Mozilla\Firefox\Preferences (Deprecated)\browser.search.update
   ```
3. Verify that the setting is configured as "Enabled"

Alternatively, you can check the registry:

1. Open the Registry Editor
2. Navigate to:
   ```
   HKLM\SOFTWARE\Policies\Mozilla\Firefox\Preferences
   ```
3. Verify that the `browser.search.update` value exists and is set to `1` (DWORD)

### Linux:

Firefox policies on Linux are typically managed through a JSON configuration file.

1. Locate the policy file (usually in `/etc/firefox/policies/`)
2. Check for the following configuration:
   ```json
   {
     "policies": {
       "Preferences": {
         "browser.search.update": true
       }
     }
   }
   ```

## Remediation

To remediate this issue:

### Windows:

1. Download and install the Firefox Group Policy template (firefox.admx/adml) from [Mozilla's policy templates repository](https://github.com/mozilla/policy-templates/releases)
2. Open the Group Policy Management Console
3. Navigate to:
   ```
   Computer Configuration\Policies\Administrative Templates\Mozilla\Firefox\Preferences (Deprecated)
   ```
4. Double-click on "browser.search.update"
5. Set the policy to "Enabled"
6. Click "Apply" and "OK"

### Linux:

1. Create or edit the Firefox policy file (e.g., `/etc/firefox/policies/policies.json`)
2. Ensure it contains the following configuration:
   ```json
   {
     "policies": {
       "Preferences": {
         "browser.search.update": true
       }
     }
   }
   ```
3. Save the file and restart Firefox for the changes to take effect

For both Windows and Linux, it's recommended to implement an automated process to regularly audit and enforce this configuration across all managed devices.