# (L1) Ensure 'Do not allow proxy settings to be changed' is set to 'Enabled'

## Description

This policy setting configures whether users can change proxy settings in Mozilla Firefox. The recommended state for this setting is: Enabled.

When this setting is not properly configured, users can modify Firefox's proxy settings, potentially bypassing company-wide proxy configurations. This can lead to several issues:

1. Reduced security: Data might not be routed through the company's proxy, jeopardizing security measures.
2. Monitoring issues: Corporate systems may fail to track network traffic from affected users.
3. Compliance violations: Bypassing proxy servers could lead to non-compliance issues depending on industry regulations or company policies.
4. Performance issues: Manual proxy settings might lead to suboptimal routing or connection times.

The root cause of this issue is typically the absence of the necessary group policy template (`.admx`/`.adml` files) for this specific Firefox policy.

## Audit

To audit this setting:

1. Open the Group Policy Management Console (gpmc.msc)
2. Navigate to the following UI path:
   ```
   Computer Configuration\Policies\Administrative Templates\Mozilla\Firefox\Proxy Settings\Do not allow proxy settings to be changed
   ```
3. Verify that the setting is configured as "Enabled"

Alternatively, you can check the registry:

1. Open the Registry Editor (regedit.exe)
2. Navigate to the following key:
   ```
   HKLM\SOFTWARE\Policies\Mozilla\Firefox\EnableTrackingProtection
   ```
3. Verify that the "Locked" value exists and is set to 1 (REG_DWORD)

## Remediation

### Windows

1. Download the Firefox Group Policy template (firefox.admx/adml) from:
   https://github.com/mozilla/policy-templates/releases

2. Copy the downloaded .admx file to:
   ```
   C:\Windows\PolicyDefinitions\
   ```

3. Copy the downloaded .adml file to the appropriate language subfolder, e.g.:
   ```
   C:\Windows\PolicyDefinitions\en-US\
   ```

4. Open the Group Policy Management Console (gpmc.msc)

5. Navigate to:
   ```
   Computer Configuration\Policies\Administrative Templates\Mozilla\Firefox\Proxy Settings\Do not allow proxy settings to be changed
   ```

6. Set the policy to "Enabled"

7. Run `gpupdate /force` from an elevated command prompt to apply the changes

### Linux

For Linux environments using Firefox, the process is different as Group Policy is a Windows-specific technology. However, you can achieve similar results using Firefox's policy files:

1. Create a JSON file named `policies.json` in one of these locations:
   - `/etc/firefox/policies/`
   - `/usr/lib/firefox/distribution/`

2. Add the following content to the file:
   ```json
   {
     "policies": {
       "ProxySettings": {
         "Locked": true
       }
     }
   }
   ```

3. Save the file and restart Firefox for the changes to take effect.

4. To verify, open Firefox and go to `about:policies`. You should see the proxy settings policy listed as enforced.

Remember to implement proper file permissions to prevent unauthorized modifications to the policy file.