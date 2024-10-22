# (L1) Ensure 'NTLM' is set to 'Disabled'

## Description

NT LAN Manager (NTLM) v1 is an outdated authentication protocol that contains significant cryptographic weaknesses. When enabled, it exposes systems to potential credential theft and unauthorized access. This vulnerability specifically targets the use of NTLM v1 in Mozilla Firefox.

Key points:
- NTLM v1 is susceptible to cryptographic attacks
- Disabling NTLM v1 eliminates this initial attack vector
- This configuration change is specific to Firefox, not system-wide
- Compatibility with older applications may be affected

## Audit

To audit this setting:

1. Open the Group Policy Management Console
2. Navigate to: Computer Configuration > Policies > Administrative Templates > Mozilla > Firefox > Authentication
3. Locate the "NTLM" setting
4. Verify that it is set to "Disabled"

Alternatively, you can check the following registry key:

```
HKLM\SOFTWARE\Policies\Mozilla\Firefox\Authentication\NTLM
```

The setting is correctly configured if this registry value does not exist.

## Remediation

### Windows

1. Ensure you have the required Group Policy template (firefox.admx/adml) installed. If not, download it from the official Mozilla repository.

2. Open the Group Policy Management Console

3. Navigate to: Computer Configuration > Policies > Administrative Templates > Mozilla > Firefox > Authentication

4. Locate and open the "NTLM" setting

5. Set it to "Disabled"

6. Click "Apply" and then "OK"

7. Run `gpupdate /force` from an elevated command prompt to apply the changes

### Linux

Firefox on Linux typically doesn't use Group Policy. Instead, you can disable NTLM v1 for Firefox by:

1. Locate the Firefox configuration file (usually `prefs.js` in the Firefox profile directory)

2. Add or modify the following line:

   ```
   user_pref("network.auth.use-ntlm", false);
   ```

3. Save the file and restart Firefox

Note: For enterprise deployments on Linux, consider using a centralized configuration management system to deploy this setting across multiple machines.

Remember to thoroughly test this change in a controlled environment before deploying it widely, as it may impact compatibility with some older applications or services.