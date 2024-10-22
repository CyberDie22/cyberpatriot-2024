# (L1) Ensure 'Offer to save logins' is set to 'Disabled'

## Description

Firefox allows for credentials to be stored in its credential store for certain websites. This configuration poses a security risk as attackers with local privileges may gain access to stored login credentials. The vulnerability is categorized as medium to high severity, depending on the level of access an attacker might obtain:

- **Medium:** If an attacker has access to standard user accounts, they could compromise credentials for that user.
- **High:** If an attacker gains administrative or system-level privileges, they could potentially access and steal credentials for all users on the system.

The impact of this vulnerability could result in:

- Compromise of user credentials for various websites
- Unauthorized access to sensitive data, accounts, or services
- Potential data breaches, financial losses, or reputational damage

It's important to note that while disabling this feature reduces risk, it should be implemented alongside other security measures such as strong passwords, robust access controls, and comprehensive threat monitoring.

## Audit

To audit this setting:

1. Open the Group Policy Management Console (GPMC) on a domain controller or a system with the Group Policy Management tools installed.

2. Navigate to the following path:
   ```
   Computer Configuration\Policies\Administrative Templates\Mozilla\Firefox
   ```

3. Locate the "Offer to save logins" setting.

4. Verify that it is set to "Disabled".

Alternatively, you can check the registry:

1. Open the Registry Editor (regedit.exe) with administrative privileges.

2. Navigate to the following key:
   ```
   HKLM\SOFTWARE\Policies\Mozilla\Firefox
   ```

3. Look for a DWORD value named "OfferToSaveLogins".

4. Verify that its value is set to 0.

## Remediation

To remediate this vulnerability:

### Windows:

1. Download and install the Firefox ADMX/ADML template from: https://github.com/mozilla/policy-templates/releases

2. Open the Group Policy Management Console (GPMC).

3. Create a new Group Policy Object (GPO) or edit an existing one.

4. Navigate to the following path:
   ```
   Computer Configuration\Policies\Administrative Templates\Mozilla\Firefox
   ```

5. Locate and double-click on the "Offer to save logins" setting.

6. Select "Disabled".

7. Click "Apply" and then "OK".

8. Update Group Policy on target machines using the command:
   ```
   gpupdate /force
   ```

### Linux:

For Linux systems, Firefox settings are typically managed through a `policies.json` file:

1. Create or edit the file `/usr/lib/firefox/distribution/policies.json` (location may vary based on distribution).

2. Add or modify the following content:
   ```json
   {
     "policies": {
       "OfferToSaveLogins": false
     }
   }
   ```

3. Save the file and restart Firefox for the changes to take effect.

4. For system-wide deployment, consider using configuration management tools like Ansible, Puppet, or Chef to distribute this configuration file to all managed systems.