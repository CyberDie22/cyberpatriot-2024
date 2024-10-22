# (L1) Ensure 'security.mixed_content.block_active_content' is set to 'Enabled'

## Description

This policy setting configures Firefox to block active mixed content, such as JavaScript, CSS, objects, and xhr requests loaded over HTTP on HTTPS pages. Mixed content occurs when a webpage containing secure HTTPS content also utilizes insecure HTTP resources, creating an attack vector for Man-in-the-Middle (MitM) attacks.

When this policy is not enforced, an attacker could potentially intercept and manipulate these insecure resources without the user's knowledge. This can lead to various security risks, including:

- Redirection to fake websites
- Injection of malware
- Extraction of sensitive information

By enabling this policy, you ensure that Firefox blocks active mixed content, mitigating the risk of MitM attacks and maintaining the integrity and confidentiality of data exchanged during browsing sessions.

## Audit

To audit this setting, follow these steps:

1. Open the Group Policy Management Console (GPMC) on a domain controller or a system with the Group Policy Management tools installed.

2. Navigate to the following path:
   ```
   Computer Configuration\Policies\Administrative Templates\Mozilla\Firefox\Preferences (Deprecated)
   ```

3. Locate the policy setting "security.mixed_content.block_active_content".

4. Verify that the policy is set to "Enabled".

Alternatively, you can check the registry:

1. Open the Registry Editor (regedit.exe).

2. Navigate to the following registry key:
   ```
   HKLM\SOFTWARE\Policies\Mozilla\Firefox\Preferences
   ```

3. Verify that the "security.mixed_content.block_active_content" value exists and is set to 1 (REG_DWORD).

For Linux systems:

1. Check the Firefox configuration file (usually located at `/etc/firefox/policies/policies.json`).

2. Verify that the following entry exists and is set to true:
   ```json
   {
     "policies": {
       "Preferences": {
         "security.mixed_content.block_active_content": true
       }
     }
   }
   ```

## Remediation

To implement this policy setting, follow these steps:

For Windows systems:

1. Download and install the Firefox Group Policy template (firefox.admx/adml) from: https://github.com/mozilla/policy-templates/releases

2. Open the Group Policy Management Console (GPMC).

3. Create or edit a Group Policy Object (GPO) linked to the organizational unit (OU) containing the systems you want to configure.

4. Navigate to the following path:
   ```
   Computer Configuration\Policies\Administrative Templates\Mozilla\Firefox\Preferences (Deprecated)
   ```

5. Double-click on the "security.mixed_content.block_active_content" policy setting.

6. Set the policy to "Enabled".

7. Click "Apply" and then "OK".

8. Run `gpupdate /force` on target systems to apply the new policy immediately.

For Linux systems:

1. Create or edit the Firefox policy file at `/etc/firefox/policies/policies.json`.

2. Add or modify the following content:
   ```json
   {
     "policies": {
       "Preferences": {
         "security.mixed_content.block_active_content": true
       }
     }
   }
   ```

3. Save the file and ensure it has the correct permissions (readable by all users).

4. Restart Firefox on all affected systems for the changes to take effect.

Note: Ensure that you test this policy in a controlled environment before deploying it widely, as it may affect the functionality of some websites that rely on mixed content.