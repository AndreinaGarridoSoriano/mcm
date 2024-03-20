# -*- coding: utf-8 -*-
# **************************************************************************
# *
# * Authors:     you (you@yourinstitution.email)
# *
# * your institution
# *
# * This program is free software; you can redistribute it and/or modify
# * it under the terms of the GNU General Public License as published by
# * the Free Software Foundation; either version 2 of the License, or
# * (at your option) any later version.
# *
# * This program is distributed in the hope that it will be useful,
# * but WITHOUT ANY WARRANTY; without even the implied warranty of
# * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# * GNU General Public License for more details.
# *
# * You should have received a copy of the GNU General Public License
# * along with this program; if not, write to the Free Software
# * Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA
# * 02111-1307  USA
# *
# *  All comments concerning this program package may be sent to the
# *  e-mail address 'you@yourinstitution.email'
# *
# **************************************************************************


"""
Describe your python module here:
This module will provide the traditional Hello world example
"""
from enum import Enum

from pyworkflow.constants import BETA
import pyworkflow.protocol.params as params
from pyworkflow.utils import Message
from pyworkflow.object import Integer
from pwem.protocols import EMProtocol


class outputs(Enum):
    count = Integer


class MCMPrefixHelloWorld(EMProtocol):

    _label = 'MCM'
    _devStatus = BETA
    _possibleOutputs = outputs

    # -------------------------- DEFINE param functions ----------------------
    def _defineParams(self, form):
        """ Define the input parameters that will be used.
        Params:
            form: this is the form to be populated with sections and params.
        """
        # You need a params to belong to a section:
        form.addSection(label=Message.LABEL_INPUT)

        form.addParam('alpha', params.FloatParam,
                      validators=[params.Positive],
                      default=,
                      label='Alpha', important=True,
                      help='Strength of image gradient')

        form.addParam('beta', params.FloatParam,
                      validators=[params.Positive],
                      default=,
                      label='Beta', important=True,
                      help='Mean curvature')

    # --------------------------- STEPS functions ------------------------------
    def _insertAllSteps(self):
        # Insert processing steps
        self._insertFunctionStep(self.greetingsStep)
        self._insertFunctionStep(self.createOutputStep)

    def validateValues(self):
        if not (0 <= self.alpha <= 1):
            raise ValueError("Parameter alpha needs to be between 0 and 1 but is: {}".format(arg.alpha))


    def greetingsStep(self):
        # say what the parameter says!!
        for time in range(0, self.times.get()):
            print(self.alpha)

    def createOutputStep(self):
        # register how many times the message has been printed
        # Now count will be an accumulated value
        timesPrinted = Integer(self.times.get() + self.previousCount.get())

        self._defineOutputs(**{outputs.count.name: timesPrinted})
        self._defineSourceRelation(self.message, timesPrinted)

    # --------------------------- INFO functions -----------------------------------
    def _validate(self):
        errors = []

        if self.times > 20:
            errors.append("Cannot do more than 20 times.")

        return errors

    def _summary(self):
        """ Summarize what the protocol has done"""
        summary = []

        if self.isFinished():
            summary.append(f"This protocol has printed *{self.message}* {self.times} times.")
        return summary

    def _methods(self):
        methods = []

        if self.isFinished():
            methods.append(f"{self.message} has been printed in this run {self.times} times.")
            if self.previousCount.hasPointer():
                methods.append("Accumulated count from previous runs were %i."
                               " In total, %s messages has been printed."
                               % (self.previousCount, self.count))
        return methods
