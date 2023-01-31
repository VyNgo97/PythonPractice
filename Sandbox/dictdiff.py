def detect_data_changes(params_data: dict, prev_data: dict) -> bool:
    changes = False
    if prev_data is None or params_data is None:
        return changes

    for key, value in params_data.items():
        if (value is not None) and (value != prev_data.get(key)):
            changes = True
            return changes
    return changes

curr = {
          "activebit": "TRUE",
          "addresslist": {
            "address": {
              "address1": "3339 Ehrlich Rd",
              "address2": None,
              "cell": None,
              "city": "Tampa",
              "country": "US",
              "county": None,
              "email": None,
              "ext": None,
              "ext2": None,
              "fax": None,
              "phone": None,
              "phone2": None,
              "state": "FL",
              "type": "REGULAR",
              "zip": "33618-2507"
            }
          },
          "allowpartialpayment": "N",
          "billingname": "RPA MAINTENANCE",
          "buildingnumber": None,
          "cellphone": None,
          "contactstatus": "Lease signer",
          "cosignerbit": "FALSE",
          "curlateamt": "0.00",
          "donotrenew": "N",
          "estfutchgs": "0.00",
          "faxnumber": None,
          "filteredaddresslist": None,
          "finalcollection": "N",
          "guarantorbit": "FALSE",
          "haspets": "N",
          "hohbit": "TRUE",
          "homephone": "(813) 569-7575",
          "incollection": "N",
          "inevict": "N",
          "inpaymentplan": "N",
          "integration_property_id": "4974402",
          "leaseid": "417",
          "leasesigneddate": None,
          "leasetype": None,
          "moveindate": None,
          "noach": None,
          "nochk": "N",
          "nomoneyorder": "N",
          "occupantbit": "FALSE",
          "pendingbalance": "0.00",
          "propertynumber": "4974402",
          "propertynumberid": "1",
          "residentagestatus": "Unknown",
          "residenthouseholdid": "381",
          "residentsincedate": None,
          "residenttype": "H",
          "screeningstatus": {
            "resultdate": None,
            "screeningresult": "Not Screened",
            "screeningresultcode": None
          },
          "signerbit": "TRUE",
          "unitid": None,
          "workphone": None
        }

prev = {
          "activebit": "TRUE",
          "addresslist": {
            "address": {
              "address1": "3339 Ehrlich Rd",
              "address2": None,
              "cell": None,
              "city": "Tampa",
              "country": "US",
              "county": None,
              "email": None,
              "ext": None,
              "ext2": None,
              "fax": None,
              "phone": None,
              "phone2": None,
              "state": "FL",
              "type": "REGULAR",
              "zip": "33618-2507"
            }
          },
          "allowpartialpayment": "N",
          "billingname": "RPA MAINTENANCE",
          "buildingnumber": None,
          "cellphone": None,
          "contactstatus": "Lease signer",
          "cosignerbit": "FALSE",
          "curlateamt": "0.00",
          "donotrenew": "N",
          "estfutchgs": "0.00",
          "faxnumber": None,
          "filteredaddresslist": None,
          "finalcollection": "N",
          "guarantorbit": "FALSE",
          "haspets": "N",
          "hohbit": "TRUE",
          "homephone": "(813) 569-7575",
          "incollection": "N",
          "inevict": "N",
          "inpaymentplan": "N",
          "integration_property_id": "4974402",
          "leaseid": "417",
          "leasesigneddate": None,
          "leasetype": None,
          "moveindate": None,
          "noach": None,
          "nochk": "N",
          "nomoneyorder": "N",
          "occupantbit": "FALSE",
          "pendingbalance": "0.00",
          "propertynumber": "4974402",
          "propertynumberid": "1",
          "residentagestatus": "Unknown",
          "residenthouseholdid": "381",
          "residentsincedate": None,
          "residenttype": "H",
          "screeningstatus": {
            "resultdate": None,
            "screeningresult": "Not Screened",
            "screeningresultcode": None
          },
          "signerbit": "TRUE",
          "unitid": None,
          "workphone": None
        }

print(detect_data_changes(prev, curr))