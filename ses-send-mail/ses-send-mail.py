
def function(mail_vars):
        print("Source={} ".format(mail_vars["SOURCE"]))


mail_vars = {
    SENDER = "Sender Name <ecano@equisens.es>",
    "SOURCE": "ecano@equisens.es"
}

function(mail_vars)