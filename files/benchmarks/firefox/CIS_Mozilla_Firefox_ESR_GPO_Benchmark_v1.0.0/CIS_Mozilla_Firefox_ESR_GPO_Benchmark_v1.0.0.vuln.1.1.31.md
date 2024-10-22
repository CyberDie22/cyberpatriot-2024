## Description

Firefox's "Form Fill Assistance" feature allows the browser to save data entered into forms by users, facilitating faster future interactions. However, this convenience comes with potential security risks. The vulnerability lies in the possibility of unintended data leakage rather than a direct exploit. By disabling the "Form Fill Assistance" feature, we can prevent Firefox from saving this potentially sensitive form data, thus reducing the risk of unauthorized access to this information.

The recommended state for this setting is: Enabled (which effectively disables the Form Fill Assistance feature).

## Audit

To audit this setting:

### Windows:
1. Open the Registry Editor (regedit.exe)
2. Navigate to the following key:
   ```
   HKLM\SOFTWARE\Policies\Mozilla\Firefox
   ```
3. Verify that the `DisableFormHistory` value exists and is set to `1` (REG_DWORD)

### Linux:
Firefox policies on Linux are typically managed through a JSON file. To audit:

1. Check for the existence of the policy file:
   ```
   /usr/lib/firefox/distribution/policies.json
   ```
2. If the file exists, verify it contains the following:
   ```json
   {
     "policies": {
       "DisableFormHistory": true
     }
   }
   ```

## Remediation

To remediate this vulnerability:

### Windows:
1. Download the Firefox Group Policy template (firefox.admx/adml) from: https://github.com/mozilla/policy-templates/releases
2. Install the template in your Group Policy Central Store or local machine
3. Open the Group Policy Management Console
4. Navigate to: Computer Configuration > Policies > Administrative Templates > Mozilla > Firefox
5. Set the "Disable Form History" policy to "Enabled"

Alternatively, you can set the registry value directly:
1. Open the Registry Editor (regedit.exe)
2. Navigate to:
   ```
   HKLM\SOFTWARE\Policies\Mozilla\Firefox
   ```
3. Create a new DWORD value named `DisableFormHistory` and set it to `1`

### Linux:
1. Create or edit the file:
   ```
   /usr/lib/firefox/distribution/policies.json
   ```
2. Ensure the file contains the following content:
   ```json
   {
     "policies": {
       "DisableFormHistory": true
     }
   }
   ```
3. Save the file and restart Firefox for the changes to take effect

Note: Ensure you have the necessary permissions to modify system files when performing these actions on Linux.