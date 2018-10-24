# -*- coding: utf-8 -*-
from odoo import http

# class MeetingroomBooking(http.Controller):
#     @http.route('/meetingroom_booking/meetingroom_booking/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/meetingroom_booking/meetingroom_booking/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('meetingroom_booking.listing', {
#             'root': '/meetingroom_booking/meetingroom_booking',
#             'objects': http.request.env['meetingroom_booking.meetingroom_booking'].search([]),
#         })

#     @http.route('/meetingroom_booking/meetingroom_booking/objects/<model("meetingroom_booking.meetingroom_booking"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('meetingroom_booking.object', {
#             'object': obj
#         })