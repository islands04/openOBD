from measure.measure import Measure
from thermo.ithermodevice import IThermoDevice
from accelerometer.iacceldevice import IAccelDevice
from gps.igpsdevice import IGPSDevice
from obd.iobddevice import IOBDDevice

import abc


class IDeviceCollection(abc.ABC):

	@abc.abstractmethod
	def __init__(self, thermoDevice: IThermoDevice, gpsDevice: IGPSDevice, accelDevice: IAccelDevice, obdDevice: IOBDDevice):
		pass

	@abc.abstractmethod
	def read_current_data(self, message: str) -> Measure:
		"""message must be a string from DeviceConstants or MeasureConstants"""
		pass

	@abc.abstractmethod
	def init_devices(self, devicelist):
		pass