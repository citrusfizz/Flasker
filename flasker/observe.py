from urlparse import urlparse
import urllib2, urllib, sys



def observeAccount(account):
    account = ''
    password = ''
    ret = account
    if len(str(account)) > 6:
        acct = urlparse(account)
        account = acct.path.split('/')[2]
        print account
    masterAccount = '/api/accounts/60072'
    apiurl = 'https://us-3.rightscale.com/api/session'


    params = {
                'email': email,
                'password': password,
                'account_href': masterAccount
    }
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "X_API_VERSION": "1.5"
    }


    req1 = urllib2.Request(apiurl, urllib.urlencode(params), headers)
    response = urllib2.urlopen(req1)
    #print response.headers

    cookie = response.headers.get('Set-Cookie')
    if response.headers.get('Status') == '204 No Content':
        accessurl = 'https://us-3.rightscale.com/global//admin_accounts/' + str(account) + '/access'
        #print accessurl
        headers2 = {
                'Host': 'us-3.rightscale.com',
                'Referer': 'https://us-3.rightscale.com/global//admin_accounts/'+ str(account),
                'cookie': cookie
        }
        req2 = urllib2.Request(accessurl,'', headers2)
        response2 = urllib2.urlopen(req2)
        if response2.headers.get('Status') == '200 OK':
            return "you should now be able to access %s" % ret
        else:
            print "something Failed"
        #print "something failed"
        #print response.headers.get('Status')
        #print response.headers
        #if response2.headers.

    else:
        print response.headers.get('Status')
        print response.headers
    #print cookie


if __name__ == "__main__":
   #observeAccount(sys.argv[1],sys.argv[2],sys.argv[3])
    ac = 27915
    email = ""
    password = ''
    a = observeAccount(ac, email, password)
    print a

