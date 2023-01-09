from functools import reduce
import pickle
from os.path import dirname

f = open('dstu_tables', 'rb')
multtable = pickle.load(f)

Pi = [
    [
        ['A8', '43', '5F', '06', '6B', '75', '6C', '59', '71', 'DF', '87', '95', '17', 'F0', 'D8', '09'],
        ['6D', 'F3', '1D', 'CB', 'C9', '4D', '2C', 'AF', '79', 'E0', '97', 'FD', '6F', '4B', '45', '39'],
        ['3E', 'DD', 'A3', '4F', 'B4', 'B6', '9A', '0E', '1F', 'BF', '15', 'E1', '49', 'D2', '93', 'C6'],
        ['92', '72', '9E', '61', 'D1', '63', 'FA', 'EE', 'F4', '19', 'D5', 'AD', '58', 'A4', 'BB', 'A1'],
        ['DC', 'F2', '83', '37', '42', 'E4', '7A', '32', '9C', 'CC', 'AB', '4A', '8F', '6E', '04', '27'],
        ['2E', 'E7', 'E2', '5A', '96', '16', '23', '2B', 'C2', '65', '66', '0F', 'BC', 'A9', '47', '41'],
        ['34', '48', 'FC', 'B7', '6A', '88', 'A5', '53', '86', 'F9', '5B', 'DB', '38', '7B', 'C3', '1E'],
        ['22', '33', '24', '28', '36', 'C7', 'B2', '3B', '8E', '77', 'BA', 'F5', '14', '9F', '08', '55'],
        ['9B', '4C', 'FE', '60', '5C', 'DA', '18', '46', 'CD', '7D', '21', 'B0', '3F', '1B', '89', 'FF'],
        ['EB', '84', '69', '3A', '9D', 'D7', 'D3', '70', '67', '40', 'B5', 'DE', '5D', '30', '91', 'B1'],
        ['78', '11', '01', 'E5', '00', '68', '98', 'A0', 'C5', '02', 'A6', '74', '2D', '0B', 'A2', '76'],
        ['B3', 'BE', 'CE', 'BD', 'AE', 'E9', '8A', '31', '1C', 'EC', 'F1', '99', '94', 'AA', 'F6', '26'],
        ['2F', 'EF', 'E8', '8C', '35', '03', 'D4', '7F', 'FB', '05', 'C1', '5E', '90', '20', '3D', '82'],
        ['F7', 'EA', '0A', '0D', '7E', 'F8', '50', '1A', 'C4', '07', '57', 'B8', '3C', '62', 'E3', 'C8'],
        ['AC', '52', '64', '10', 'D0', 'D9', '13', '0C', '12', '29', '51', 'B9', 'CF', 'D6', '73', '8D'],
        ['81', '54', 'C0', 'ED', '4E', '44', 'A7', '2A', '85', '25', 'E6', 'CA', '7C', '8B', '56', '80'],
    ],
    [
        ['CE', 'BB', 'EB', '92', 'EA', 'CB', '13', 'C1', 'E9', '3A', 'D6', 'B2', 'D2', '90', '17', 'F8'],
        ['42', '15', '56', 'B4', '65', '1C', '88', '43', 'C5', '5C', '36', 'BA', 'F5', '57', '67', '8D'],
        ['31', 'F6', '64', '58', '9E', 'F4', '22', 'AA', '75', '0F', '02', 'B1', 'DF', '6D', '73', '4D'],
        ['7C', '26', '2E', 'F7', '08', '5D', '44', '3E', '9F', '14', 'C8', 'AE', '54', '10', 'D8', 'BC'],
        ['1A', '6B', '69', 'F3', 'BD', '33', 'AB', 'FA', 'D1', '9B', '68', '4E', '16', '95', '91', 'EE'],
        ['4C', '63', '8E', '5B', 'CC', '3C', '19', 'A1', '81', '49', '7B', 'D9', '6F', '37', '60', 'CA'],
        ['E7', '2B', '48', 'FD', '96', '45', 'FC', '41', '12', '0D', '79', 'E5', '89', '8C', 'E3', '20'],
        ['30', 'DC', 'B7', '6C', '4A', 'B5', '3F', '97', 'D4', '62', '2D', '06', 'A4', 'A5', '83', '5F'],
        ['2A', 'DA', 'C9', '00', '7E', 'A2', '55', 'BF', '11', 'D5', '9C', 'CF', '0E', '0A', '3D', '51'],
        ['7D', '93', '1B', 'FE', 'C4', '47', '09', '86', '0B', '8F', '9D', '6A', '07', 'B9', 'B0', '98'],
        ['18', '32', '71', '4B', 'EF', '3B', '70', 'A0', 'E4', '40', 'FF', 'C3', 'A9', 'E6', '78', 'F9'],
        ['8B', '46', '80', '1E', '38', 'E1', 'B8', 'A8', 'E0', '0C', '23', '76', '1D', '25', '24', '05'],
        ['F1', '6E', '94', '28', '9A', '84', 'E8', 'A3', '4F', '77', 'D3', '85', 'E2', '52', 'F2', '82'],
        ['50', '7A', '2F', '74', '53', 'B3', '61', 'AF', '39', '35', 'DE', 'CD', '1F', '99', 'AC', 'AD'],
        ['72', '2C', 'DD', 'D0', '87', 'BE', '5E', 'A6', 'EC', '04', 'C6', '03', '34', 'FB', 'DB', '59'],
        ['B6', 'C2', '01', 'F0', '5A', 'ED', 'A7', '66', '21', '7F', '8A', '27', 'C7', 'C0', '29', 'D7'],
    ],
    [
        ['93', 'D9', '9A', 'B5', '98', '22', '45', 'FC', 'BA', '6A', 'DF', '02', '9F', 'DC', '51', '59'],
        ['4A', '17', '2B', 'C2', '94', 'F4', 'BB', 'A3', '62', 'E4', '71', 'D4', 'CD', '70', '16', 'E1'],
        ['49', '3C', 'C0', 'D8', '5C', '9B', 'AD', '85', '53', 'A1', '7A', 'C8', '2D', 'E0', 'D1', '72'],
        ['A6', '2C', 'C4', 'E3', '76', '78', 'B7', 'B4', '09', '3B', '0E', '41', '4C', 'DE', 'B2', '90'],
        ['25', 'A5', 'D7', '03', '11', '00', 'C3', '2E', '92', 'EF', '4E', '12', '9D', '7D', 'CB', '35'],
        ['10', 'D5', '4F', '9E', '4D', 'A9', '55', 'C6', 'D0', '7B', '18', '97', 'D3', '36', 'E6', '48'],
        ['56', '81', '8F', '77', 'CC', '9C', 'B9', 'E2', 'AC', 'B8', '2F', '15', 'A4', '7C', 'DA', '38'],
        ['1E', '0B', '05', 'D6', '14', '6E', '6C', '7E', '66', 'FD', 'B1', 'E5', '60', 'AF', '5E', '33'],
        ['87', 'C9', 'F0', '5D', '6D', '3F', '88', '8D', 'C7', 'F7', '1D', 'E9', 'EC', 'ED', '80', '29'],
        ['27', 'CF', '99', 'A8', '50', '0F', '37', '24', '28', '30', '95', 'D2', '3E', '5B', '40', '83'],
        ['B3', '69', '57', '1F', '07', '1C', '8A', 'BC', '20', 'EB', 'CE', '8E', 'AB', 'EE', '31', 'A2'],
        ['73', 'F9', 'CA', '3A', '1A', 'FB', '0D', 'C1', 'FE', 'FA', 'F2', '6F', 'BD', '96', 'DD', '43'],
        ['52', 'B6', '08', 'F3', 'AE', 'BE', '19', '89', '32', '26', 'B0', 'EA', '4B', '64', '84', '82'],
        ['6B', 'F5', '79', 'BF', '01', '5F', '75', '63', '1B', '23', '3D', '68', '2A', '65', 'E8', '91'],
        ['F6', 'FF', '13', '58', 'F1', '47', '0A', '7F', 'C5', 'A7', 'E7', '61', '5A', '06', '46', '44'],
        ['42', '04', 'A0', 'DB', '39', '86', '54', 'AA', '8C', '34', '21', '8B', 'F8', '0C', '74', '67'],
    ],
    [
        ['68', '8D', 'CA', '4D', '73', '4B', '4E', '2A', 'D4', '52', '26', 'B3', '54', '1E', '19', '1F'],
        ['22', '03', '46', '3D', '2D', '4A', '53', '83', '13', '8A', 'B7', 'D5', '25', '79', 'F5', 'BD'],
        ['58', '2F', '0D', '02', 'ED', '51', '9E', '11', 'F2', '3E', '55', '5E', 'D1', '16', '3C', '66'],
        ['70', '5D', 'F3', '45', '40', 'CC', 'E8', '94', '56', '08', 'CE', '1A', '3A', 'D2', 'E1', 'DF'],
        ['B5', '38', '6E', '0E', 'E5', 'F4', 'F9', '86', 'E9', '4F', 'D6', '85', '23', 'CF', '32', '99'],
        ['31', '14', 'AE', 'EE', 'C8', '48', 'D3', '30', 'A1', '92', '41', 'B1', '18', 'C4', '2C', '71'],
        ['72', '44', '15', 'FD', '37', 'BE', '5F', 'AA', '9B', '88', 'D8', 'AB', '89', '9C', 'FA', '60'],
        ['EA', 'BC', '62', '0C', '24', 'A6', 'A8', 'EC', '67', '20', 'DB', '7C', '28', 'DD', 'AC', '5B'],
        ['34', '7E', '10', 'F1', '7B', '8F', '63', 'A0', '05', '9A', '43', '77', '21', 'BF', '27', '09'],
        ['C3', '9F', 'B6', 'D7', '29', 'C2', 'EB', 'C0', 'A4', '8B', '8C', '1D', 'FB', 'FF', 'C1', 'B2'],
        ['97', '2E', 'F8', '65', 'F6', '75', '07', '04', '49', '33', 'E4', 'D9', 'B9', 'D0', '42', 'C7'],
        ['6C', '90', '00', '8E', '6F', '50', '01', 'C5', 'DA', '47', '3F', 'CD', '69', 'A2', 'E2', '7A'],
        ['A7', 'C6', '93', '0F', '0A', '06', 'E6', '2B', '96', 'A3', '1C', 'AF', '6A', '12', '84', '39'],
        ['E7', 'B0', '82', 'F7', 'FE', '9D', '87', '5C', '81', '35', 'DE', 'B4', 'A5', 'FC', '80', 'EF'],
        ['CB', 'BB', '6B', '76', 'BA', '5A', '7D', '78', '0B', '95', 'E3', 'AD', '74', '98', '3B', '36'],
        ['64', '6D', 'DC', 'F0', '59', 'A9', '4C', '17', '7F', '91', 'B8', 'C9', '57', '1B', 'E0', '61'],
    ]
]

_Pi = [
    [
        ['A4', 'A2', 'A9', 'C5', '4E', 'C9', '03', 'D9', '7E', '0F', 'D2', 'AD', 'E7', 'D3', '27', '5B'],
        ['E3', 'A1', 'E8', 'E6', '7C', '2A', '55', '0C', '86', '39', 'D7', '8D', 'B8', '12', '6F', '28'],
        ['CD', '8A', '70', '56', '72', 'F9', 'BF', '4F', '73', 'E9', 'F7', '57', '16', 'AC', '50', 'C0'],
        ['9D', 'B7', '47', '71', '60', 'C4', '74', '43', '6C', '1F', '93', '77', 'DC', 'CE', '20', '8C'],
        ['99', '5F', '44', '01', 'F5', '1E', '87', '5E', '61', '2C', '4B', '1D', '81', '15', 'F4', '23'],
        ['D6', 'EA', 'E1', '67', 'F1', '7F', 'FE', 'DA', '3C', '07', '53', '6A', '84', '9C', 'CB', '02'],
        ['83', '33', 'DD', '35', 'E2', '59', '5A', '98', 'A5', '92', '64', '04', '06', '10', '4D', '1C'],
        ['97', '08', '31', 'EE', 'AB', '05', 'AF', '79', 'A0', '18', '46', '6D', 'FC', '89', 'D4', 'C7'],
        ['FF', 'F0', 'CF', '42', '91', 'F8', '68', '0A', '65', '8E', 'B6', 'FD', 'C3', 'EF', '78', '4C'],
        ['CC', '9E', '30', '2E', 'BC', '0B', '54', '1A', 'A6', 'BB', '26', '80', '48', '94', '32', '7D'],
        ['A7', '3F', 'AE', '22', '3D', '66', 'AA', 'F6', '00', '5D', 'BD', '4A', 'E0', '3B', 'B4', '17'],
        ['8B', '9F', '76', 'B0', '24', '9A', '25', '63', 'DB', 'EB', '7A', '3E', '5C', 'B3', 'B1', '29'],
        ['F2', 'CA', '58', '6E', 'D8', 'A8', '2F', '75', 'DF', '14', 'FB', '13', '49', '88', 'B2', 'EC'],
        ['E4', '34', '2D', '96', 'C6', '3A', 'ED', '95', '0E', 'E5', '85', '6B', '40', '21', '9B', '09'],
        ['19', '2B', '52', 'DE', '45', 'A3', 'FA', '51', 'C2', 'B5', 'D1', '90', 'B9', 'F3', '37', 'C1'],
        ['0D', 'BA', '41', '11', '38', '7B', 'BE', 'D0', 'D5', '69', '36', 'C8', '62', '1B', '82', '8F'],
    ],
    [
        ['83', 'F2', '2A', 'EB', 'E9', 'BF', '7B', '9C', '34', '96', '8D', '98', 'B9', '69', '8C', '29'],
        ['3D', '88', '68', '06', '39', '11', '4C', '0E', 'A0', '56', '40', '92', '15', 'BC', 'B3', 'DC'],
        ['6F', 'F8', '26', 'BA', 'BE', 'BD', '31', 'FB', 'C3', 'FE', '80', '61', 'E1', '7A', '32', 'D2'],
        ['70', '20', 'A1', '45', 'EC', 'D9', '1A', '5D', 'B4', 'D8', '09', 'A5', '55', '8E', '37', '76'],
        ['A9', '67', '10', '17', '36', '65', 'B1', '95', '62', '59', '74', 'A3', '50', '2F', '4B', 'C8'],
        ['D0', '8F', 'CD', 'D4', '3C', '86', '12', '1D', '23', 'EF', 'F4', '53', '19', '35', 'E6', '7F'],
        ['5E', 'D6', '79', '51', '22', '14', 'F7', '1E', '4A', '42', '9B', '41', '73', '2D', 'C1', '5C'],
        ['A6', 'A2', 'E0', '2E', 'D3', '28', 'BB', 'C9', 'AE', '6A', 'D1', '5A', '30', '90', '84', 'F9'],
        ['B2', '58', 'CF', '7E', 'C5', 'CB', '97', 'E4', '16', '6C', 'FA', 'B0', '6D', '1F', '52', '99'],
        ['0D', '4E', '03', '91', 'C2', '4D', '64', '77', '9F', 'DD', 'C4', '49', '8A', '9A', '24', '38'],
        ['A7', '57', '85', 'C7', '7C', '7D', 'E7', 'F6', 'B7', 'AC', '27', '46', 'DE', 'DF', '3B', 'D7'],
        ['9E', '2B', '0B', 'D5', '13', '75', 'F0', '72', 'B6', '9D', '1B', '01', '3F', '44', 'E5', '87'],
        ['FD', '07', 'F1', 'AB', '94', '18', 'EA', 'FC', '3A', '82', '5F', '05', '54', 'DB', '00', '8B'],
        ['E3', '48', '0C', 'CA', '78', '89', '0A', 'FF', '3E', '5B', '81', 'EE', '71', 'E2', 'DA', '2C'],
        ['B8', 'B5', 'CC', '6E', 'A8', '6B', 'AD', '60', 'C6', '08', '04', '02', 'E8', 'F5', '4F', 'A4'],
        ['F3', 'C0', 'CE', '43', '25', '1C', '21', '33', '0F', 'AF', '47', 'ED', '66', '63', '93', 'AA'],
    ],
    [
        ['45', 'D4', '0B', '43', 'F1', '72', 'ED', 'A4', 'C2', '38', 'E6', '71', 'FD', 'B6', '3A', '95'],
        ['50', '44', '4B', 'E2', '74', '6B', '1E', '11', '5A', 'C6', 'B4', 'D8', 'A5', '8A', '70', 'A3'],
        ['A8', 'FA', '05', 'D9', '97', '40', 'C9', '90', '98', '8F', 'DC', '12', '31', '2C', '47', '6A'],
        ['99', 'AE', 'C8', '7F', 'F9', '4F', '5D', '96', '6F', 'F4', 'B3', '39', '21', 'DA', '9C', '85'],
        ['9E', '3B', 'F0', 'BF', 'EF', '06', 'EE', 'E5', '5F', '20', '10', 'CC', '3C', '54', '4A', '52'],
        ['94', '0E', 'C0', '28', 'F6', '56', '60', 'A2', 'E3', '0F', 'EC', '9D', '24', '83', '7E', 'D5'],
        ['7C', 'EB', '18', 'D7', 'CD', 'DD', '78', 'FF', 'DB', 'A1', '09', 'D0', '76', '84', '75', 'BB'],
        ['1D', '1A', '2F', 'B0', 'FE', 'D6', '34', '63', '35', 'D2', '2A', '59', '6D', '4D', '77', 'E7'],
        ['8E', '61', 'CF', '9F', 'CE', '27', 'F5', '80', '86', 'C7', 'A6', 'FB', 'F8', '87', 'AB', '62'],
        ['3F', 'DF', '48', '00', '14', '9A', 'BD', '5B', '04', '92', '02', '25', '65', '4C', '53', '0C'],
        ['F2', '29', 'AF', '17', '6C', '41', '30', 'E9', '93', '55', 'F7', 'AC', '68', '26', 'C4', '7D'],
        ['CA', '7A', '3E', 'A0', '37', '03', 'C1', '36', '69', '66', '08', '16', 'A7', 'BC', 'C5', 'D3'],
        ['22', 'B7', '13', '46', '32', 'E8', '57', '88', '2B', '81', 'B2', '4E', '64', '1C', 'AA', '91'],
        ['58', '2E', '9B', '5C', '1B', '51', '73', '42', '23', '01', '6E', 'F3', '0D', 'BE', '3D', '0A'],
        ['2D', '1F', '67', '33', '19', '7B', '5E', 'EA', 'DE', '8B', 'CB', 'A9', '8C', '8D', 'AD', '49'],
        ['82', 'E4', 'BA', 'C3', '15', 'D1', 'E0', '89', 'FC', 'B1', 'B9', 'B5', '07', '79', 'B8', 'E1'],
    ],
    [
        ['B2', 'B6', '23', '11', 'A7', '88', 'C5', 'A6', '39', '8F', 'C4', 'E8', '73', '22', '43', 'C3'],
        ['82', '27', 'CD', '18', '51', '62', '2D', 'F7', '5C', '0E', '3B', 'FD', 'CA', '9B', '0D', '0F'],
        ['79', '8C', '10', '4C', '74', '1C', '0A', '8E', '7C', '94', '07', 'C7', '5E', '14', 'A1', '21'],
        ['57', '50', '4E', 'A9', '80', 'D9', 'EF', '64', '41', 'CF', '3C', 'EE', '2E', '13', '29', 'BA'],
        ['34', '5A', 'AE', '8A', '61', '33', '12', 'B9', '55', 'A8', '15', '05', 'F6', '03', '06', '49'],
        ['B5', '25', '09', '16', '0C', '2A', '38', 'FC', '20', 'F4', 'E5', '7F', 'D7', '31', '2B', '66'],
        ['6F', 'FF', '72', '86', 'F0', 'A3', '2F', '78', '00', 'BC', 'CC', 'E2', 'B0', 'F1', '42', 'B4'],
        ['30', '5F', '60', '04', 'EC', 'A5', 'E3', '8B', 'E7', '1D', 'BF', '84', '7B', 'E6', '81', 'F8'],
        ['DE', 'D8', 'D2', '17', 'CE', '4B', '47', 'D6', '69', '6C', '19', '99', '9A', '01', 'B3', '85'],
        ['B1', 'F9', '59', 'C2', '37', 'E9', 'C8', 'A0', 'ED', '4F', '89', '68', '6D', 'D5', '26', '91'],
        ['87', '58', 'BD', 'C9', '98', 'DC', '75', 'C0', '76', 'F5', '67', '6B', '7E', 'EB', '52', 'CB'],
        ['D1', '5B', '9F', '0B', 'DB', '40', '92', '1A', 'FA', 'AC', 'E4', 'E1', '71', '1F', '65', '8D'],
        ['97', '9E', '95', '90', '5D', 'B7', 'C1', 'AF', '54', 'FB', '02', 'E0', '35', 'BB', '3A', '4D'],
        ['AD', '2C', '3D', '56', '08', '1B', '4A', '93', '6A', 'AB', 'B8', '7A', 'F2', '7D', 'DA', '3F'],
        ['FE', '3E', 'BE', 'EA', 'AA', '44', 'C6', 'D0', '36', '48', '70', '96', '77', '24', '53', 'DF'],
        ['F3', '83', '28', '32', '45', '1E', 'A4', 'D3', 'A2', '46', '6E', '9C', 'DD', '63', 'D4', '9D'],
    ]
]


def log(msg, matrix):
    print(f'{msg}')
    for row in matrix:
        print(f'   {row[0]} {row[1]} ')


def string_to_unicode_string(string):
    unicode_string = ''
    for char in string:
        unicode_string += hex(ord(char))[2:].upper().zfill(2)

    return unicode_string


def unicode_string_to_matrix(unicode_string):
    state = []
    col_1 = unicode_string[:int(len(unicode_string) / 2)]
    col_2 = unicode_string[int(len(unicode_string) / 2):]
    for i in range(8):
        state.append([col_1[(i*2):(i*2+2)], col_2[(i*2):(i*2+2)]])

    return state


def matrix_to_unicode_string(matrix):
    unicode_string = ''
    for i in range(2):
        for j in range(8):
            unicode_string += (matrix[j][i])

    return unicode_string


def unicode_string_to_string(string):
    ASCII_values = []
    for i in range(int(len(string) / 2)):
        ASCII_values.append(string[i * 2: i * 2 + 2])
    ASCII_string = "".join([chr(int(value, 16)) for value in ASCII_values])

    return ASCII_string


def add_round_key(state, round_key, func_type="plus", inverse=False):
    if func_type == "plus":
        if inverse:
            for i in range(2):
                _state_col = '1'
                _round_key_col = ''
                for j in range(8):
                    _state_col += state[7 - j][i]
                    _round_key_col += round_key[7 - j][i]
                _state_col_res = hex(int(_state_col, 16) - int(_round_key_col, 16))[::-1][:16][::-1]
                for j in range(8):
                    state[7-j][i] = _state_col_res[(j*2):(j*2+2)]
        else:
            for i in range(2):
                _state_col = ''
                _round_key_col = ''
                for j in range(8):
                    _state_col += state[7 - j][i]
                    _round_key_col += round_key[7 - j][i]
                _state_col_res = hex(int(_state_col, 16) + int(_round_key_col, 16))[::-1][:16][::-1]
                for j in range(8):
                    state[7 - j][i] = _state_col_res[(j * 2):(j * 2 + 2)]
    elif func_type == "xor":
        for i in range(8):
            for j in range(2):
                _tmp = int(state[i][j], 16) ^ int(round_key[i][j], 16)
                state[i][j] = hex(_tmp % 256)[2:].upper().zfill(2)

    return state


def transformation_eta(state, inverse=False):
    for i in range(8):
        for j in range(2):
            current = state[i][j]
            if not inverse:
                state[i][j] = Pi[i % 4][int(current[0], base=16)][int(current[1], base=16)]
            else:
                state[i][j] = _Pi[i % 4][int(current[0], base=16)][int(current[1], base=16)]

    return state


def transformation_tau(state):
    for i in range(4, 8):
        state[i].append(state[i][0])
        state[i].pop(0)
    return state


def transformation_psi(x, inverse=False):
    def rightshiftvector(x, i):
        l = len(x)
        i = i % l
        return x[l - i:] + x[:l - i]

    def scalar_mult(x, y):
        res = 0
        for i in range(len(x)):
            res ^= multtable[int(x[i], 16)][y[i]]
        return res

    _x = []

    for i in range(2):
        for j in range(8):
            _x.append(x[j][i])
    if not inverse:
        v = [0x01, 0x01, 0x05, 0x01, 0x08, 0x06, 0x07, 0x04]
    else:
        v = [0xAD, 0x95, 0x76, 0xA8, 0x2F, 0x49, 0xD7, 0xCA]

    res = []
    for i in range(2):
        for j in range(8):
            res.append(hex(scalar_mult(_x[i * 8:i * 8 + 8], rightshiftvector(v, j)))[2:].upper().zfill(2))

    _res = []
    col_1 = res[:int(len(res) / 2)]
    col_2 = res[int(len(res) / 2):]
    for i in range(8):
        _res.append([col_1[i], col_2[i]])

    return _res


def dstu_7624_2014_encode(plain_text, _K0, _K1):
    print(f'\n1. Обрано довільній текст довжиною 16 літер: {plain_text}')

    unicode_string = string_to_unicode_string(plain_text)
    print(f'Кожну літеру заміняємо відповідним шістнадцятирічним ASCII-кодом: {unicode_string}')

    G0 = unicode_string_to_matrix(unicode_string)
    log('Формуємо матрицю - 2 стовпця по 8 шістнадцятирічних числа та отримуємо початковий State G_0:', G0)

    K0 = unicode_string_to_matrix(_K0)
    log(f'За заданим 128-бітним ключем нульового раунду (K_0 = "{_K0}") формуємо відповідну State матрицю – 2 стовпця по 8 шістнадцятирічних числа:', K0)

    G1 = add_round_key(G0, K0, func_type="plus", inverse=False)
    log('Обчислюємо функцію η додавання раундового ключа K_0 і початкового внутрішнього стану G_0. Новий State познаємо G_1:', G1)

    G2 = transformation_eta(G1)
    log('2. Обчислюємо функцію підстановки π для кожного елементу матриці State G_1. Новий State познаємо G_2:', G2)

    G3 = transformation_tau(G2)
    log('3. Обчислюємо функцію зсуву τ для рядків матриці State G_2. Новий State познаємо G_3:', G3)

    G4 = transformation_psi(G3)
    log('4. Обчислюємо функцію ψ лінійного перетворення стовпців матриці State G_3. Новий State познаємо G_4:', G4)

    K1 = unicode_string_to_matrix(_K1)
    log(f'5. За заданим 128-бітним ключем першого раунду (K_1 = "{_K1}") формуємо відповідну State матрицю – 2 стовпця по 8 шістнадцятирічних числа:', K1)

    G5 = add_round_key(K1, G4, func_type="xor")
    log('Обчислюємо функцію к додавання раундового ключа K_1 і початкового внутрішнього стану G_4 за модулем 2. Кінцевий State познаємо G`:', G5)

    G = matrix_to_unicode_string(G5)
    print(f'6. Перетворюємо кінцевий внутрішній стан G` на текст: {G}')

    return G


def dstu_7624_2014_decode(encrypted_unicode_string, _K0, _K1):
    _G = unicode_string_to_matrix(encrypted_unicode_string)

    K1 = unicode_string_to_matrix(_K1)
    log(f'За заданим 128-бітним ключем першого раунду (K_1 = "{_K1}") формуємо відповідну State матрицю – 2 стовпця по 8 шістнадцятирічних числа:', K1)

    print('Знайдємо відкритий текст повідомлення T.')
    print('Для цього:')

    _G4 = add_round_key(K1, _G, func_type="xor")
    log('Обчислюємо функцію к` додавання раундового ключа K_1 і внутрішнього стану G`_5 за модулем 2. Новий State познаємо G`_4:', _G4)

    _G3 = transformation_psi(_G4, inverse=True)
    log('Обчислюємо функцію ψ` оберненого лінійного перетворення стовпців матриці State G`_4. Новий State познаємо G`_3:', _G3)

    _G2 = transformation_tau(_G3)
    log('Обчислюємо обернену функцію зсуву τ` для рядків матриці State G`_3. Новий State познаємо G`_2:', _G2)

    _G1 = transformation_eta(_G2, inverse=True)
    log('Обчислюємо обернену функцію підстановки π` для кожного елементу матриці State G`_2. Новий State познаємо G`_1:', _G1)

    K0 = unicode_string_to_matrix(_K0)
    log(f'За заданим 128-бітним ключем нульового раунду (K_0 = "{_K0}") формуємо відповідну State матрицю – 2 стовпця по 8 шістнадцятирічних числа:', K0)

    _G0 = add_round_key(_G1, K0, func_type="plus", inverse=True)
    log('Обчислюємо функцію η` віднімання раундового ключа K_0 від внутрішнього стану G`_1. Новий State познаємо G`_0:', _G0)

    T = matrix_to_unicode_string(_G0)

    print(f'Перетворемо внутрішній стан G`_0 на текст T: {unicode_string_to_string(T)}')


def main():
    # Nikita
    plain_text = 'hello good world'
    _G = 'BAD27AD501351DE6AE46F6BFECADCBBA'

    # Danil
    # plain_text = 'gachimuchi test '
    # _G = '3C1985CE0469BEA729C5AD4C1F1F261E'

    # Vanya
    # plain_text = 'cryptography 128'
    # _G = '930B663CA9358FAB28B3E455C5466DE0'

    # Vadym
    # plain_text = 'lorem ipsum     '
    # _G = '2C067662AEBF0066F35F14EFC34BDB5F'

    RK0 = "16505E6B9B3AB1E6865B77DCE082A0F4"
    RK1 = "E6865B77DCE082A0F416505E6B9B3AB1"
    encrypted_text = dstu_7624_2014_encode(plain_text, RK0, RK1)

    print('\nПеревіремо коректність зашифрування обраного тексту:')
    print(f'Отримано 128-бітне зашифроване повідомлення {encrypted_text}.')
    log('Формуємо матрицю - 2 стовпця по 8 шістнадцятирічних числа та отримуємо State G`_5:', unicode_string_to_matrix(encrypted_text))
    dstu_7624_2014_decode(encrypted_text, RK0, RK1)

    # _G = unicode_string_to_matrix("726894B4D6DC4DEC8D0A4A767C7B2E1B")  # Test
    # RK0 = "17161514131211101F1E1D1C1B1A1918"  # Test
    # RK1 = "0102030405060708090A0B0C0D0E0F00"  # Test

    print(f'\n7. Отримано 128-бітне зашифроване повідомлення {_G}. Після 9-того раунду розшифрування обчислено State G (згідно з номером варіанту N).')
    log('Формуємо матрицю - 2 стовпця по 8 шістнадцятирічних числа та отримуємо State G`_5:', unicode_string_to_matrix(_G))
    dstu_7624_2014_decode(_G, RK0, RK1)


if __name__ == "__main__":
    main()
    # W # Acta esu fabvma" (Acta est fabŭla - Представление окончено)

    # V # Eventvs!doceu! (Eventus docet - Событие учит)

    # D # Otia daot viuja/ (Otia dant vitia - Праздность рождает пороки)

    # N # Wax oo, wax ogf"