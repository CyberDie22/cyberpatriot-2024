# (L1) Ensure 'Block pop-ups from websites' is set to 'Enabled'

## Description

This vulnerability relates to the configuration of the Firefox pop-up blocker when deployed through Group Policy. The recommended state for this setting is 'Enabled', but if misconfigured, it could leave systems exposed to potential malicious pop-up attacks.

The vulnerability stems from:

1. Incorrect Group Policy configuration, leading to the pop-up blocker being disabled.
2. Missing or improperly deployed Group Policy Template (`.admx`/`.adml`) files, which are required to create the policy object in the Group Policy editor.

If the pop-up blocker is disabled, it increases the risk of:

- Phishing attacks: Malicious actors could deploy pop-up windows to steal login credentials or redirect users to fraudulent websites.
- Malware distribution: Pop-up windows can be used to install malicious software onto the system.
- Other security exploits: Pop-up windows are a common mechanism for carrying out a wide range of attacks.

## Audit

To audit this setting:

1. Open the Group Policy Management Editor.
2. Navigate to Computer Configuration > Policies > Administrative Templates > Mozilla > Firefox > Popups
3. Verify that "Block pop-ups from websites" is set to "Enabled".

Alternatively, you can check the registry:

1. Open the Registry Editor.
2. Navigate to `HKLM\SOFTWARE\Policies\Mozilla\Firefox\PopupBlocking`
3. Verify that the `Default` value is set to `1` (REG_DWORD).

If the Group Policy setting is not available or the registry key is missing, it indicates that the necessary Group Policy template files may not be properly deployed.

## Remediation

### Windows:

1. Download the Firefox Group Policy templates (firefox.admx/adml) from the official Mozilla website.
2. Copy the `.admx` file to `C:\Windows\PolicyDefinitions` and the `.adml` file to the appropriate language subfolder (e.g., `C:\Windows\PolicyDefinitions\en-US` for English).
3. Open the Group Policy Management Editor.
4. Navigate to Computer Configuration > Policies > Administrative Templates > Mozilla > Firefox > Popups
5. Double-click on "Block pop-ups from websites".
6. Select "Enabled".
7. Click "Apply" and then "OK".

### Linux:

Firefox on Linux typically doesn't use Group Policy. However, you can achieve similar results by:

1. Open a terminal.
2. Navigate to the Firefox installation directory (usually `/usr/lib/firefox` or `/opt/firefox`).
3. Create or edit the `distribution/policies.json` file:

   ```bash
   sudo mkdir -p distribution
   sudo nano distribution/policies.json
   ```

4. Add the following content to the file:

   ```json
   {
     "policies": {
       "PopupBlocking": {
         "Default": true
       }
     }
   }
   ```

5. Save the file and exit the editor.
6. Restart Firefox for the changes to take effect.

Remember to test these changes in a controlled environment before deploying them widely to ensure they don't negatively impact your users' workflows.