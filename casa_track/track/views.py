from django.shortcuts import render, redirect
from .forms import TrackingFormForm
from .models import TrackingForm
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseForbidden, HttpResponseNotAllowed
from django.conf import settings
from django.core.mail import send_mail, BadHeaderError, EmailMessage

from weasyprint import HTML
# from django.template.loader import render_to_string\

def home(request):
    if request.user.is_superuser:
        t_forms = TrackingForm.objects.all().order_by('-created_at')
        context = {
            't_forms': t_forms,
            'admin': True,
        }
        return render(request, 'track/user_admin.html', context)
    else:
        return render(request, 'track/home.html')


"""
   Uses Django emailing service: https://docs.djangoproject.com/en/2.1/topics/email/
"""


def tracking(request):
    if request.method == "POST":
        form = TrackingFormForm(request.POST)
        if form.is_valid():
            form.save()

            supervisor = form.cleaned_data['supervisor']
            super_email = map_to_supervisor(supervisor)
            advocate = form.cleaned_data['advocate']
            subject = "[CASA Track] New Tracking Form from " + advocate
            from_email = settings.EMAIL_HOST_USER
            html_message = get_html_message(form)

            email = EmailMessage(subject, html_message, from_email, [super_email])
            pdf_generation(request, html_message)
            email.attach_file('mypdf.pdf')
            email.content_subtype = "html"
            email.send()
            
            return redirect('/') # submitted :D page
        else:
            print(form.errors)
    else:
        form = TrackingFormForm()
    return render(request, 'track/tracking.html', {'form': form})


def pdf_generation(request, html_source):

    # TODO make this a template
    # paragraphs = ['first paragraph', 'second paragraph', 'third paragraph']
    # html_string = render_to_string('track/pdf.html', {'paragraphs': paragraphs})
    HTML(string=html_source).write_pdf(target='mypdf.pdf')


# TODO make this a template
def get_html_message(form):  # all form data passed
    return """<html>
  <head>
    <meta name="viewport" content="width=device-width">
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    <title>Simple Transactional Email</title>
    <style>
    /* -------------------------------------
        INLINED WITH htmlemail.io/inline
    ------------------------------------- */
    /* -------------------------------------
        RESPONSIVE AND MOBILE FRIENDLY STYLES
    ------------------------------------- */
    @media only screen and (max-width: 620px) {
      table[class=body] h1 {
        font-size: 28px !important;
        margin-bottom: 10px !important;
      }
      table[class=body] p,
            table[class=body] ul,
            table[class=body] ol,
            table[class=body] td,
            table[class=body] span,
            table[class=body] a {
        font-size: 16px !important;
      }
      table[class=body] .wrapper,
            table[class=body] .article {
        padding: 10px !important;
      }
      table[class=body] .content {
        padding: 0 !important;
      }
      table[class=body] .container {
        padding: 0 !important;
        width: 100% !important;
      }
      table[class=body] .main {
        border-left-width: 0 !important;
        border-radius: 0 !important;
        border-right-width: 0 !important;
      }
      table[class=body] .btn table {
        width: 100% !important;
      }
      table[class=body] .btn a {
        width: 100% !important;
      }
      table[class=body] .img-responsive {
        height: auto !important;
        max-width: 100% !important;
        width: auto !important;
      }
    }
    /* -------------------------------------
        PRESERVE THESE STYLES IN THE HEAD
    ------------------------------------- */
    @media all {
      .ExternalClass {
        width: 100%;
      }
      .ExternalClass,
            .ExternalClass p,
            .ExternalClass span,
            .ExternalClass font,
            .ExternalClass td,
            .ExternalClass div {
        line-height: 100%;
      }
      .apple-link a {
        color: inherit !important;
        font-family: inherit !important;
        font-size: inherit !important;
        font-weight: inherit !important;
        line-height: inherit !important;
        text-decoration: none !important;
      }
      .btn-primary table td:hover {
        background-color: #34495e !important;
      }
      .btn-primary a:hover {
        background-color: #34495e !important;
        border-color: #34495e !important;
      }
    }
    </style>
  </head>
  <body class="" style="background-image: linear-gradient(#155da1, #64ab8a); font-family: sans-serif; -webkit-font-smoothing: antialiased; font-size: 14px; line-height: 1.4; margin: 0; padding: 0; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%;">
    <table border="0" cellpadding="0" cellspacing="0" class="body" style="border-collapse: separate; mso-table-lspace: 0pt; mso-table-rspace: 0pt; width: 100%; background-image: linear-gradient(#155da1, #64ab8a);">
      <tr>
        <td style="font-family: sans-serif; font-size: 14px; vertical-align: top;">&nbsp;</td>
        <td class="container" style="font-family: sans-serif; font-size: 14px; vertical-align: top; display: block; Margin: 0 auto; max-width: 580px; padding: 10px; width: 580px;">
          <div class="content" style="box-sizing: border-box; display: block; Margin: 0 auto; max-width: 580px; padding: 10px;">

            <!-- START CENTERED WHITE CONTAINER -->
            <span class="preheader" style="color: transparent; display: none; height: 0; max-height: 0; max-width: 0; opacity: 0; overflow: hidden; mso-hide: all; visibility: hidden; width: 0;">This is preheader text. Some clients will show this text as a preview.</span>
            <table class="main" style="border-collapse: separate; mso-table-lspace: 0pt; mso-table-rspace: 0pt; width: 100%; background: #ffffff; border-radius: 3px;">

              <!-- START MAIN CONTENT AREA -->
              <tr>
                <td class="wrapper" style="font-family: sans-serif; font-size: 14px; vertical-align: top; horizontal-align: center; box-sizing: border-box; padding: 20px;">
                  <table border="0" cellpadding="0" cellspacing="0" style="border-collapse: separate; mso-table-lspace: 0pt; mso-table-rspace: 0pt; width: 100%;">
                    <tr>
                      <td style="font-family: sans-serif; font-size: 14px; vertical-align: top;">
                        
                        <h2 style="text-align:center;">Form from CASA Track: """ + form.cleaned_data['advocate'] + """</h2>
                        <p style="text-align:center;">Supervisor: <span>""" + dict(form.fields['supervisor'].choices)[form.cleaned_data['supervisor']] + """</span></p>
                        <p style="text-align:center;">Advocate's Name: """ + form.cleaned_data['advocate'] + """</p>
                        <p style="text-align:center;">Child's Name: """ + form.cleaned_data['child_name'] + """</p>
                        <p style="text-align:center;">Month, Year: """ + form.cleaned_data['month'] + """</p>
                        <p style="text-align:center;">Hours Spent: """ + form.cleaned_data['hours_education'] + """</p>
                        <p style="text-align:center;">Additional Hours Spent on Case: """ + form.cleaned_data['hours_on_case'] + """</p>
                        <p style="text-align:center;">Continuing Education: """ + form.cleaned_data['continuing_edu'] + """</p>
                        <p style="text-align:center;">Miles Driven: """ + form.cleaned_data['miles_driven'] + """</p>
                        <p style="text-align:center;">Face-to-face Hours: """ + form.cleaned_data['face_advocate_sv_hours'] + """</p>
                        <p style="text-align:center;">Phone: """ + form.cleaned_data['phone_advocate_sv'] + """</p>
                        <img src='""" + form.cleaned_data['esignature'] + """' style='width: 500px;'>
                        </td>
                    </tr>
                  </table>
                </td>
              </tr>

            <!-- END MAIN CONTENT AREA -->
            </table>

            <!-- START FOOTER -->
            <div class="footer" style="clear: both; Margin-top: 10px; text-align: center; width: 100%;">
              <table border="0" cellpadding="0" cellspacing="0" style="border-collapse: separate; mso-table-lspace: 0pt; mso-table-rspace: 0pt; width: 100%;">
                <tr>
                  <td class="content-block powered-by" style="font-family: sans-serif; vertical-align: top; padding-bottom: 10px; padding-top: 10px; font-size: 12px; color: #FFFFFF; text-align: center;">
                    Powered by <a href="https://github.com/hack4impact-calpoly" style="color: #FFFFFF; font-size: 12px; text-align: center; text-decoration: none;">Hack4Impact Cal Poly</a>.
                  </td>
                </tr>
                <tr>
                  <td class="content-block powered-by" style="font-family: sans-serif; vertical-align: top; padding-bottom: 10px; padding-top: 10px; font-size: 12px; color: #FFFFFF; text-align: center;">
                    See a problem? <a href="mailto:calpoly@hack4impact.org?Subject=CASA%20Track%20Bug" target="_top" style="color: #FFFFFF; font-size: 12px; text-align: center;">Contact us</a>.
                  </td>
                </tr>
              </table>
            </div>
            <!-- END FOOTER -->

          <!-- END CENTERED WHITE CONTAINER -->
          </div>
        </td>
        <td style="font-family: sans-serif; font-size: 14px; vertical-align: top;">&nbsp;</td>
      </tr>
    </table>
  </body>
</html>"""


def map_to_supervisor(supervisor_char):
    if supervisor_char == 'C':
        return 'h4icptest@gmail.com'
    if supervisor_char == 'H':
        return 'h4icptest@gmail.com'
    if supervisor_char == 'G':
        return 'h4icptest@gmail.com'
    if supervisor_char == 'K':
        return 'h4icptest@gmail.com'
    if supervisor_char == 'P':
        return 'h4icptest@gmail.com'
    if supervisor_char == 'M':
        return 'h4icptest@gmail.com'
    if supervisor_char == 'N':
        return 'h4icptest@gmail.com'


def delete_form(request):
    if request.method == 'POST':
        item_id = int(request.POST.get('item_id'))
        item = TrackingForm.objects.get(id=item_id)
        if request.user.is_superuser:
            item.delete()
            return redirect('/')
        else:
            print("fail")
            return HttpResponseForbidden()
    else:
        return HttpResponseNotAllowed(request)
