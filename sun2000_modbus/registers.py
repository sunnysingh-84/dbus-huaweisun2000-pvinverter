from enum import Enum

from . import datatypes
from . import mappings


class AccessType(Enum):
    RO = "ro"
    RW = "rw"
    WO = "wo"


class Register:
    address: int
    quantity: int
    data_type: datatypes.DataType
    gain: float
    unit: str
    access_type: AccessType
    mapping: dict

    def __init__(self, address, quantity, data_type, gain, unit, access_type, mapping):
        self.address = address
        self.quantity = quantity
        self.data_type = data_type
        self.gain = gain
        self.unit = unit
        self.access_type = access_type
        self.mapping = mapping


class InverterEquipmentRegister(Enum):
    Model = Register(30000, 15, datatypes.DataType.STRING, None, None, AccessType.RO, None)
    SN = Register(30015, 10, datatypes.DataType.STRING, None, None, AccessType.RO, None)
    PN = Register(30025, 10, datatypes.DataType.STRING, None, None, AccessType.RO, None)
    ModelID = Register(30070, 1, datatypes.DataType.UINT16_BE, 1, None, AccessType.RO, None)
    NumberOfPVStrings = Register(30071, 1, datatypes.DataType.UINT16_BE, 1, None, AccessType.RO, None)
    NumberOfMPPTrackers = Register(30072, 1, datatypes.DataType.UINT16_BE, 1, None, AccessType.RO, None)
    RatedPower = Register(30073, 2, datatypes.DataType.UINT32_BE, 1, "W", AccessType.RO, None)
    MaximumActivePower = Register(30075, 2, datatypes.DataType.UINT32_BE, 1, "W", AccessType.RO, None)
    MaximumApparentPower = Register(30077, 2, datatypes.DataType.UINT32_BE, 1000, "kVA", AccessType.RO, None)
    MaximumReactivePowerFedToTheGrid = Register(30079, 2, datatypes.DataType.INT32_BE, 1000, "kvar", AccessType.RO, None)
    MaximumReactivePowerAbsorbedFromTheGrid = Register(30081, 2, datatypes.DataType.INT32_BE, 1000, "kvar", AccessType.RO, None)
    State1 = Register(32000, 1, datatypes.DataType.BITFIELD16, None, None, AccessType.RO, None)
    State2 = Register(32002, 1, datatypes.DataType.BITFIELD16, None, None, AccessType.RO, None)
    State3 = Register(32003, 2, datatypes.DataType.BITFIELD32, None, None, AccessType.RO, None)
    Alarm1 = Register(32008, 1, datatypes.DataType.BITFIELD16, None, None, AccessType.RO, None)
    Alarm2 = Register(32009, 1, datatypes.DataType.BITFIELD16, None, None, AccessType.RO, None)
    Alarm3 = Register(32010, 1, datatypes.DataType.BITFIELD16, None, None, AccessType.RO, None)
    PV1Voltage = Register(32016, 1, datatypes.DataType.INT16_BE, 10, "V", AccessType.RO, None)
    PV1Current = Register(32017, 1, datatypes.DataType.INT16_BE, 100, "A", AccessType.RO, None)
    PV2Voltage = Register(32018, 1, datatypes.DataType.INT16_BE, 10, "V", AccessType.RO, None)
    PV2Current = Register(32019, 1, datatypes.DataType.INT16_BE, 100, "A", AccessType.RO, None)
    InputPower = Register(32064, 2, datatypes.DataType.INT32_BE, 1, "W", AccessType.RO, None)
    LineVoltageBetweenPhasesAAndB = Register(32066, 1, datatypes.DataType.UINT16_BE, 10, "V", AccessType.RO, None)
    PhaseACurrent = Register(32072, 2, datatypes.DataType.INT32_BE, 1000, "A", AccessType.RO, None)
    PeakActivePowerOfCurrentDay = Register(32078, 2, datatypes.DataType.INT32_BE, 1, "W", AccessType.RO, None)
    ActivePower = Register(32080, 2, datatypes.DataType.INT32_BE, 1, "W", AccessType.RO, None)
    ReactivePower = Register(32082, 2, datatypes.DataType.INT32_BE, 1000, "kvar", AccessType.RO, None)
    PowerFactor = Register(32084, 1, datatypes.DataType.INT16_BE, 1000, None, AccessType.RO, None)
    GridFrequency = Register(32085, 1, datatypes.DataType.UINT16_BE, 100, "Hz", AccessType.RO, None)
    Efficiency = Register(32086, 1, datatypes.DataType.UINT16_BE, 100, "%", AccessType.RO, None)
    InternalTemperature = Register(32087, 1, datatypes.DataType.INT16_BE, 10, "°C", AccessType.RO, None)
    InsulationResistance = Register(32088, 1, datatypes.DataType.UINT16_BE, 1000, "MOhm", AccessType.RO, None)
    DeviceStatus = Register(32089, 1, datatypes.DataType.UINT16_BE, 1, None, AccessType.RO, mappings.DeviceStatus)
    FaultCode = Register(32090, 1, datatypes.DataType.UINT16_BE, 1, None, AccessType.RO, None)
    StartupTime = Register(32091, 2, datatypes.DataType.UINT32_BE, 1, None, AccessType.RO, None)
    ShutdownTime = Register(32093, 2, datatypes.DataType.UINT32_BE, 1, None, AccessType.RO, None)
    AccumulatedEnergyYield = Register(32106, 2, datatypes.DataType.UINT32_BE, 100, "kWh", AccessType.RO, None)
    DailyEnergyYield = Register(32114, 2, datatypes.DataType.UINT32_BE, 100, "kWh", AccessType.RO, None)
    ActiveAdjustmentMode = Register(35300, 1, datatypes.DataType.UINT16_BE, 1, None, AccessType.RO, None)
    ActiveAdjustmentValue = Register(35302, 2, datatypes.DataType.UINT32_BE, 1, None, AccessType.RO, None)
    ActiveAdjustmentCommand = Register(35303, 1, datatypes.DataType.UINT16_BE, 1, None, AccessType.RO, None)
    ReactiveAdjustmentMode = Register(35304, 1, datatypes.DataType.UINT16_BE, 1, None, AccessType.RO, None)
    ReactiveAdjustmentValue = Register(35305, 2, datatypes.DataType.UINT32_BE, 1, None, AccessType.RO, None)
    ReactiveAdjustmentCommand = Register(35307, 1, datatypes.DataType.UINT16_BE, 1, None, AccessType.RO, None)
    PowerMeterCollectionActivePower = Register(37113, 2, datatypes.DataType.INT32_BE, 1, "W", AccessType.RO, None)
    TotalNumberOfOptimizers = Register(37200, 1, datatypes.DataType.UINT16_BE, 1, None, AccessType.RO, None)
    NumberOfOnlineOptimizers = Register(37201, 1, datatypes.DataType.UINT16_BE, 1, None, AccessType.RO, None)
    FeatureData = Register(37202, 1, datatypes.DataType.UINT16_BE, 1, None, AccessType.RO, None)
    SystemTime = Register(40000, 2, datatypes.DataType.UINT32_BE, 1, None, AccessType.RW, None)
    QUCharacteristicCurveMode = Register(40037, 1, datatypes.DataType.UINT16_BE, 1, None, AccessType.RW, None)
    QUDispatchTriggerPower = Register(40038, 1, datatypes.DataType.UINT16_BE, 1, "%", AccessType.RW, None)
    FixedActivePowerDeratedInKW = Register(40120, 1, datatypes.DataType.UINT16_BE, 10, "kW", AccessType.RW, None)
    ReactivePowerCompensationInPF = Register(40122, 1, datatypes.DataType.INT16_BE, 1000, None, AccessType.RW, None)
    ReactivePowerCompensationQS = Register(40123, 1, datatypes.DataType.INT16_BE, 1000, None, AccessType.RW, None)
    ActivePowerPercentageDerating = Register(40125, 1, datatypes.DataType.UINT16_BE, 10, "%", AccessType.RW, None)
    FixedActivePowerDeratedInW = Register(40126, 2, datatypes.DataType.UINT32_BE, 1, "W", AccessType.RW, None)
    ReactivePowerCompensationAtNight = Register(40129, 2, datatypes.DataType.INT32_BE, 1000, "kvar", AccessType.RW, None)
    CosPhiPPnCharacteristicCurve = Register(40133, 21, datatypes.DataType.MULTIDATA, None, None, AccessType.RW, None)
    QUCharacteristicCurve = Register(40154, 21, datatypes.DataType.MULTIDATA, None, None, AccessType.RW, None)
    PFUCharacteristicCurve = Register(40175, 21, datatypes.DataType.MULTIDATA, None, None, AccessType.RW, None)
    ReactivePowerAdjustmentTime = Register(40196, 1, datatypes.DataType.UINT16_BE, 1, "s", AccessType.RW, None)
    QUPowerPercentageToExitScheduling = Register(40198, 1, datatypes.DataType.UINT16_BE, 1, "%", AccessType.RW, None)
    # Startup = Register(40200, 1, datatypes.DataType.UINT16_BE, 1, None, AccessType.WO, None) # disabled because not readable (AccessType.WO)
    # Shutdown = Register(40201, 1, datatypes.DataType.UINT16_BE, 1, None, AccessType.WO, None) # disabled because not readable (AccessType.WO)
    GridCode = Register(42000, 1, datatypes.DataType.UINT16_BE, 1, None, AccessType.RW, None)
    ReactivePowerChangeGradient = Register(42015, 2, datatypes.DataType.UINT32_BE, 1000, "%/s", AccessType.RW, None)
    ActivePowerChangeGradient = Register(42017, 2, datatypes.DataType.UINT32_BE, 1000, "%/s", AccessType.RW, None)
    ScheduleInstructionValidDuration = Register(42019, 2, datatypes.DataType.UINT32_BE, 1, "s", AccessType.RW, None)
    TimeZone = Register(43006, 1, datatypes.DataType.INT16_BE, 1, "min", AccessType.RW, None)


class MeterEquipmentRegister(Enum):
    MeterType = Register(37125, 1, datatypes.DataType.UINT16_BE, 1, None, AccessType.RO, mappings.MeterType)
    MeterStatus = Register(37100, 1, datatypes.DataType.UINT16_BE, 1, None, AccessType.RO, mappings.MeterStatus)
    MeterModelDetectionResult = Register(37138, 1, datatypes.DataType.UINT16_BE, 1, None, AccessType.RO, mappings.MeterModelDetectionResult)
    APhaseVoltage = Register(37101, 2, datatypes.DataType.INT32_BE, 10, "V", AccessType.RO, None)
    BPhaseVoltage = Register(37103, 2, datatypes.DataType.INT32_BE, 10, "V", AccessType.RO, None)
    CPhaseVoltage = Register(37105, 2, datatypes.DataType.INT32_BE, 10, "V", AccessType.RO, None)
    APhaseCurrent = Register(37107, 2, datatypes.DataType.INT32_BE, 100, "A", AccessType.RO, None)
    BPhaseCurrent = Register(37109, 2, datatypes.DataType.INT32_BE, 100, "A", AccessType.RO, None)
    CPhaseCurrent = Register(37111, 2, datatypes.DataType.INT32_BE, 100, "A", AccessType.RO, None)
    ActivePower = Register(37113, 2, datatypes.DataType.INT32_BE, 1, "W", AccessType.RO, None)
    ReactivePower = Register(37115, 2, datatypes.DataType.INT32_BE, 1, "var", AccessType.RO, None)
    PowerFactor = Register(37117, 1, datatypes.DataType.INT16_BE, 1000, None, AccessType.RO, None)
    GridFrequency = Register(37118, 1, datatypes.DataType.INT16_BE, 100, "Hz", AccessType.RO, None)
    PositiveActiveElectricity = Register(37119, 2, datatypes.DataType.INT32_BE, 100, "kWh", AccessType.RO, None)
    ReverseActivePower = Register(37121, 2, datatypes.DataType.INT32_BE, 100, "kWh", AccessType.RO, None)
    AccumulatedReactivePower = Register(37123, 2, datatypes.DataType.INT32_BE, 100, "kvar", AccessType.RO, None)
    ABLineVoltage = Register(37126, 2, datatypes.DataType.INT32_BE, 10, "V", AccessType.RO, None)
    BCLineVoltage = Register(37128, 2, datatypes.DataType.INT32_BE, 10, "V", AccessType.RO, None)
    CALineVoltage = Register(37130, 2, datatypes.DataType.INT32_BE, 10, "V", AccessType.RO, None)
    APhaseActivePower = Register(37132, 2, datatypes.DataType.INT32_BE, 1, "W", AccessType.RO, None)
    BPhaseActivePower = Register(37134, 2, datatypes.DataType.INT32_BE, 1, "W", AccessType.RO, None)
    CPhaseActivePower = Register(37136, 2, datatypes.DataType.INT32_BE, 1, "W", AccessType.RO, None)
