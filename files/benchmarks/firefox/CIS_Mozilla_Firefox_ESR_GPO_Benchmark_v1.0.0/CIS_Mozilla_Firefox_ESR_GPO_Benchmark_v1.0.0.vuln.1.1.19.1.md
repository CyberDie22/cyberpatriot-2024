# (L1) Ensure 'Connection Type' is set to 'Enabled: No Proxy'

## Description

Firefox can be configured to use one or more proxy servers. When a proxy server is configured for a given protocol (HTTP, FTP, Gopher, etc), Firefox will send applicable requests to that proxy server for fulfillment. This configuration guideline recommends setting Firefox to not use any proxy servers by default.

The recommended state for this setting is: Enabled: No Proxy.

**Rationale:**
Depending on the protocol used, a proxy server can access and potentially alter all information communicated between Firefox and target servers, such as websites. This poses several risks:

1. **Proxy Server Compromise:** If a proxy server is compromised, all traffic passing through it could be intercepted, analyzed, or modified.
2. **Data Leakage:** Proxy servers can be a conduit for data leakage, potentially logging and disclosing sensitive information.
3. **Unauthorized Access:** Using a proxy introduces an additional point where unauthorized access could occur.

By preventing Firefox from using proxies by default, these risks are mitigated, enhancing the security of browser communications within the enterprise environment.

## Audit

### Windows

1. Open the Group Policy Management Console (gpmc.msc).
2. Navigate to the Group Policy Object (GPO) containing the Firefox settings.
3. Expand Computer Configuration > Policies > Administrative Templates > Mozilla > Firefox > Proxy Settings.
4. Verify that the "Connection Type" setting is configured as "Enabled: No Proxy".

Alternatively, you can check the registry:

1. Open the Registry Editor (regedit.exe).
2. Navigate to the following key:
   ```
   HKLM\SOFTWARE\Policies\Mozilla\Firefox\Proxy
   ```
3. Verify that the "Mode" value is set to "none" (REG_SZ).

### Linux

For Linux systems managed by configuration management tools:

1. Check the Firefox configuration file (usually located at `/etc/firefox/policies/policies.json`).
2. Verify that the proxy settings are configured as follows:
   ```json
   {
     "policies": {
       "Proxy": {
         "Mode": "none",
         "Locked": true
       }
     }
   }
   ```

## Remediation

### Windows

To establish the recommended configuration via Group Policy:

1. Ensure you have the Mozilla Firefox Group Policy template (firefox.admx/adml) installed. If not, download it from [Mozilla's Policy Templates GitHub repository](https://github.com/mozilla/policy-templates/releases).
2. Open the Group Policy Management Console (gpmc.msc).
3. Navigate to the GPO you want to modify.
4. Go to Computer Configuration > Policies > Administrative Templates > Mozilla > Firefox > Proxy Settings.
5. Double-click on "Connection Type".
6. Set it to "Enabled" and select "No Proxy" from the dropdown.
7. Click "Apply" and then "OK".

### Linux

For Linux systems:

1. Create or edit the file `/etc/firefox/policies/policies.json`.
2. Add or modify the following content:
   ```json
   {
     "policies": {
       "Proxy": {
         "Mode": "none",
         "Locked": true
       }
     }
   }
   ```
3. Save the file and ensure it has the correct permissions (typically readable by all users but writable only by root).
4. Restart Firefox for the changes to take effect.

For both Windows and Linux, ensure that this policy is applied consistently across all systems in your enterprise environment to maintain a uniform security posture.