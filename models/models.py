from odoo import models, fields


class doctor(models.Model):
    _name = 'doctor.doctor'
    
    name = fields.Char(string="Doctor ID")
    dname = fields.Char(string="Doctor Name")
    spec = fields.Char(string="Specialisation")
    pids = fields.One2many('patient.patient', 'did',string="Patient Details")
    hos = fields.Many2many('hos.hos','docid',string="Hospital List")



class patient(models.Model):
    _name = 'patient.patient'

    pname = fields.Char(string="Patient Name")
    addrs = fields.Char(string="Patient Address")
    phno = fields.Char(string="Phone Number")
    did = fields.Many2one('doctor.doctor', string="Doctor ID")
    

class hospital(models.Model):
    _name = 'hos.hos'

    name = fields.Char(string="Hospital ID")
    hname = fields.Char(string="Hospital Name")
    hadrs = fields.Char(string="Hospital Address")
    hphone = fields.Char(string="Phone No")
    docid = fields.Many2many('doctor.doctor')

