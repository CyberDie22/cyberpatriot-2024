# (L1) Ensure 'Network Prediction' is set to 'Disabled'

## Description

Firefox's "Network Prediction" feature allows the browser to prefetch URLs without user consent. When enabled, this can lead to several security and privacy concerns in a corporate environment:

1. **Misleading Browser History**: Prefetching can cause URLs to appear in browser history that were not actually visited by the user, but merely hovered over. This can complicate forensic investigations and lead to misinterpretation of user actions.

2. **Network Leakage**: There's potential for unintended information disclosure about the local network, especially if an enterprise asset is connected to a public network. These prefetch requests could reveal internal IPs, domain names, or even application details.

3. **Unintended Requests**: Firefox may make various requests to and from networked resources, possibly including those outside the organization, without explicit user action.

The impact of this vulnerability is not about a specific attack vector, but rather the potential for indirect compromise and misinterpretation of evidence. It can also lead to unintended information leakage outside the organization's network.

## Audit

To audit this setting:

### Windows:

1. Open the Registry Editor.
2. Navigate to the following key:
   ```
   HKLM\SOFTWARE\Policies\Mozilla\Firefox
   ```
3. Check for a REG_DWORD value named "NetworkPrediction".
4. Verify that its value is set to 0.

### Linux:

1. Check the Firefox configuration file (usually located at `/etc/firefox/policies/policies.json`).
2. Look for the "NetworkPrediction" setting and ensure it's set to false.

## Remediation

To remediate this vulnerability:

### Windows:

1. Download the Firefox ADMX/ADML templates from [this link](https://github.com/mozilla/policy-templates/releases).
2. Install the templates in your Group Policy Central Store or local Policy Definitions folder.
3. Open the Group Policy Management Console.
4. Navigate to: Computer Configuration > Policies > Administrative Templates > Mozilla > Firefox
5. Locate the "Network Prediction" setting.
6. Set it to "Disabled".

### Linux:

1. Edit the Firefox policy file (usually located at `/etc/firefox/policies/policies.json`).
2. Add or modify the following entry:
   ```json
   {
     "policies": {
       "NetworkPrediction": false
     }
   }
   ```
3. Save the file and restart Firefox for the changes to take effect.

For both platforms, ensure that this setting is enforced through your organization's policy management system to prevent users from changing it.