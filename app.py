from datetime import datetime
from flask import Flask
from flask_apscheduler import APScheduler
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail, Content
import requests


app = Flask(__name__)
scheduler = APScheduler()


# A welcome message to test our server
@app.route('/')
def index():
    #res = getCryptoNews()  
    return 'hello metrnews'


# this function get crypto news from rapid api, filters the news, and put it in bula mongo database
def getCryptoNews():
        
    url = 'https://crypto-news-live3.p.rapidapi.com/news'
    headers = {
        'x-rapidapi-host': 'crypto-news-live3.p.rapidapi.com',
        'x-rapidapi-key': 'bce97ca579mshb51e03e3ca8b8b3p1587e1jsnbf4bae1e2938',
        }

    res = requests.get(url=url, headers=headers)
    if res.ok:
        res_data = res.json()
        count = 0
        news = []
    
        for i in range (len(res_data)):

            count += 1
            title = res_data[i]['title']
            news_url = res_data[i]['url']
            source = res_data[i]['source']

            news_data = {
                "title": title,
                "news_url": news_url,
                "source": source,
            }
            news.append(news_data)
            if (count == 3):
                sendMail(
                    title_1=news[0]['title'],
                    title_2=news[1]['title'],
                    title_3=news[2]['title'],
                    link_1=news[0]['news_url'],
                    link_2=news[1]['news_url'],
                    link_3=news[2]['news_url'],
                )
                print (getDate(), 'run successful')
                return



def sendMail(title_1, title_2, title_3, link_1, link_2, link_3):

    sendgrid_key = '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'    
    template = f"""
    <!DOCTYPE html>
        <html>
        <head>
            <title></title>
            <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <meta http-equiv="X-UA-Compatible" content="IE=edge" />
        </head>
        <body style="background-color: #fefefe; margin: 0 !important; padding: 0 !important;">
            <!-- HIDDEN PREHEADER TEXT -->
            <!-- div style="display: none; font-size: 1px; color: #fefefe; line-height: 1px; font-family: 'Lato', Helvetica, Arial, sans-serif; max-height: 0px; max-width: 0px; opacity: 0; overflow: hidden;"> We're thrilled to have you here! Get ready to dive into your new account. -->
            <!-- /div -->
            <table border="0" cellpadding="0" cellspacing="0" width="100%">
                <!-- LOGO -->
                <tr>
                    <td bgcolor="#499fef" align="center">
                        <table border="0" cellpadding="0" cellspacing="0" width="100%" style="max-width: 600px;">
                            <tr>
                                <td align="center" valign="top" style="padding: 40px 10px 40px 10px;"> </td>
                            </tr>
                        </table>
                    </td>
                </tr>
                <tr>
                    <td bgcolor="#499fef" align="center" style="padding: 0px 10px 0px 10px;">
                        <table border="0" cellpadding="0" cellspacing="0" width="100%" style="max-width: 600px;">
                            <tr>
                                <td bgcolor="#ffffff" align="center" valign="top" style="padding: 40px 20px 20px 20px; border-radius: 4px 4px 0px 0px; color: #111111; font-family: 'Lato', Helvetica, Arial, sans-serif; font-size: 48px; font-weight: 400; letter-spacing: 4px; line-height: 48px;">
                                    <h1 style="font-size: 18px; font-weight: 400; margin: 2;">Oluwafemi, here are your top picks for today</h1>
                                </td>
                            </tr>
                        </table>
                    </td>
                </tr>
                <tr>
                    <td bgcolor="#f4f4f4" align="center" style="padding: 0px 10px 0px 10px;">
                        <table border="0" cellpadding="0" cellspacing="0" width="100%" style="max-width: 600px;">
                            <tr>
                                <td bgcolor="#ffffff" align="left" style="padding: 20px 30px 10px 30px; color: #666666; font-family: 'Lato', Helvetica, Arial, sans-serif; font-size: 16px; font-weight: 400; line-height: 25px;">
                                    <p style="margin: 0;">{title_1}</p>
                                </td>
                            </tr>
                            <tr>
                                <td bgcolor="#ffffff" align="left" style="padding: 0px 30px 40px 30px;">
                                    <table border="0" cellspacing="0" cellpadding="0">
                                        <tr>
                                            <td align="center" style="border-radius: 3px;" bgcolor="#499fef"><a href="{link_1}" target="_blank" style="font-size: 14px; font-family: Helvetica, Arial, sans-serif; color: #ffffff; text-decoration: none; color: #ffffff; text-decoration: none; padding: 15px 25px; display: inline-block;">Read here</a></td>
                                        </tr>
                                    </table>
                                </td>
                            </tr>

                            <tr>
                                <td bgcolor="#ffffff" align="left" style="padding: 20px 30px 10px 30px; color: #666666; font-family: 'Lato', Helvetica, Arial, sans-serif; font-size: 16px; font-weight: 400; line-height: 25px;">
                                    <p style="margin: 0;">{title_2}</p>
                                </td>
                            </tr>
                            <tr>
                                <td bgcolor="#ffffff" align="left" style="padding: 0px 30px 40px 30px;">
                                    <table border="0" cellspacing="0" cellpadding="0">
                                        <tr>
                                            <td align="center" style="border-radius: 3px;" bgcolor="#499fef"><a href="{link_2}" target="_blank" style="font-size: 14px; font-family: Helvetica, Arial, sans-serif; color: #ffffff; text-decoration: none; color: #ffffff; text-decoration: none; padding: 15px 25px; display: inline-block;">Read here</a></td>
                                        </tr>
                                    </table>
                                </td>
                            </tr>

                            <tr>
                                <td bgcolor="#ffffff" align="left" style="padding: 20px 30px 10px 30px; color: #666666; font-family: 'Lato', Helvetica, Arial, sans-serif; font-size: 16px; font-weight: 400; line-height: 25px;">
                                    <p style="margin: 0;">{title_3}</p>
                                </td>
                            </tr>
                            <tr>
                                <td bgcolor="#ffffff" align="left" style="padding: 0px 30px 60px 30px;">
                                    <table border="0" cellspacing="0" cellpadding="0">
                                        <tr>
                                            <td align="center" style="border-radius: 3px;" bgcolor="#499fef"><a href="{link_3}" target="_blank" style="font-size: 14px; font-family: Helvetica, Arial, sans-serif; color: #ffffff; text-decoration: none; color: #ffffff; text-decoration: none; padding: 15px 25px; display: inline-block;">Read here</a></td>
                                        </tr>
                                    </table>
                                </td>
                            </tr>
                           
                        </table>
                    </td>
                </tr>
                
                <tr>
                    <td bgcolor="#f4f4f4" align="center" style="padding: 0px 10px 0px 10px;">
                        <table border="0" cellpadding="0" cellspacing="0" width="100%" style="max-width: 600px;">
                            <tr>
                                <td bgcolor="#f4f4f4" align="left" style="padding: 0px 30px 30px 30px; color: #666666; font-family: 'Lato', Helvetica, Arial, sans-serif; font-size: 14px; font-weight: 400; line-height: 18px;"> <br>
                                    <p style="text-align: center;">&copy; MetrNews 2022</p>
                                </td>
                            </tr>
                        </table>
                    </td>
                </tr>
            </table>
        </body>
        </html>
    """
   

    message = Mail(
        from_email = 'dev@oopatrick.com',
        to_emails = 'olarewajuoluwafemi34@gmail.com',
        subject = 'MertrNews for ' + getDate(),
        html_content = Content("text/html", content=template)
        )

    try:
        sg = SendGridAPIClient(api_key=sendgrid_key)
        response = sg.send(message)
        print(response.status_code, response.body, response.headers)

    except Exception as e:
        print(e.message)



def getDate():
    date = datetime.utcnow().date().strftime('%a %b %d')
    return date



if __name__ == '__main__':

    scheduler.add_job(id='news', func=getCryptoNews, trigger="cron", hour=5)
    scheduler.start()
    app.run(threaded=True, port=5003)
