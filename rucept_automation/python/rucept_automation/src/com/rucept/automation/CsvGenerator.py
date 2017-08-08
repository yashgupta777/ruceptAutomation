import csv
import os
import time

import config_data.Constants as Constants
import Utils

constants = Constants.Constants()
utils = Utils.Utils()

class CSVGenerator:
    def __init__(self):
        self.data = []
    
    @staticmethod
    def initCSV(csv_out_path, csv_name):
        with open(csv_out_path + "/" + csv_name, "wb") as f:
            writer = csv.writer(f)
            # writer.writerows(constants.getAmazonCSVColumns())
            writer.writerows(constants.get_amazon_csv_base1_row())
            writer.writerows(constants.get_amazon_csv_base2_row())
            writer.writerows(constants.get_amazon_csv_base3_row())

    @classmethod
    def get_csv_name(cls, operation_name):
        return str(operation_name + str(time.strftime("%Y_%m_%d")) + ".csv")
        
    @classmethod
    def generate_amazon_csv(cls, operation_name, csv_out_path, csv_name, phone_name, dsn_image_name, product_image):
        
        # modifying this parameter deliberatly as earlier for every request a csv was being generated
        # which later on switched to generate a combined csv file
        csv_name = cls.get_csv_name(operation_name)
        
        filename = csv_out_path + "/" + csv_name
        if not os.path.exists(filename):
            cls.initCSV(csv_out_path, csv_name)
        
        with open(filename, "a") as file:
            writer = csv.writer(file)
            
            a = [[]]
            row = a[0]
            row.append(cls.get_sku(phone_name))
            # row.append(cls.fill_modal_in_row(phn_image=phone_name))
            cls.fill_empty_values_in_row(row, 2)
            row.append(cls.fill_item_name_in_row(dsn_image_name, phone_name))
            print dsn_image_name
            print phone_name
            row.append(cls.fill_brand_name_in_row(brand='Kesi'))
            row.append(cls.fill_manufacturer_in_row(y='Rucept Designs'))
            row.append(cls.fill_product_description_in_row(
                z='Constructed with a plastic back, this case features a high quality printing. Snap it on the back of your phone to provide a robust protection, while keeping it colourful and classy. Made to fit Phone Case.'))
	    row.append(cls.fill_item_type_in_row(item_type='Phone Case'))
            row.append(cls.fill_feed_product_type_in_row(xx='PhoneAccessory'))
            row.append(cls.get_sku(phone_name))
            row.append(cls.get_sku(phone_name))
            row.append(cls.fill_update_delete_in_row(update='update'))
            row.append(cls.fill_standard_price_in_row(stndprice='799'))
            # row.append(cls.fill_currency_in_row(currency= 'INR'))
            row.append(cls.fill_quantity_in_row(quantity='20'))
            row.append(cls.fill_condition_type_in_row(cndttype='New'))
            cls.fill_empty_values_in_row(row, 2)
            row.append(cls.fill_selling_price_in_row(sellingprice='699'))
            row.append(cls.fill_sell_start_date_in_row(startDate='2016-10-10'))
            row.append(cls.fill_sell_end_date_in_row(endDate='2017-10-10'))
            cls.fill_empty_values_in_row(row, 1)
            row.append(cls.fill_fulfillment_latency_in_row(fulfillment='3'))
            cls.fill_empty_values_in_row(row, 12)
            row.append(cls.fill_item_dimensions_unit_of_measure_in_row(item_dimensions_unit_of_measure='CM'))
            row.append(cls.fill_item_weight_in_row(item_weight='30'))
            row.append(cls.fill_item_weight_unit_of_measure_in_row(item_weight_unit_of_measure='GR'))
            cls.fill_empty_values_in_row(row, 2)
            row.append(cls.fill_bullet_point1_in_row(bullet_point1='Designed to fit Phhones.'))
            row.append(cls.fill_bullet_point2_in_row(
                bullet_point2='Protects your cell phone from scratches and dusts in daily use.'))
            row.append(cls.fill_bullet_point3_in_row(bullet_point3='High Quality 3D Printed Back Cover.'))
            row.append(cls.fill_bullet_point4_in_row(bullet_point4='Material: ABS Plastic.'))
            row.append(cls.fill_bullet_point5_in_row(bullet_point5='Durable'))
            row.append(cls.fill_recommended_browse_nodes_in_row(recommended_browse_nodes='1389409031'))
            row.append(cls.fill_generic_keywords1_in_row(
                generic_keywords1='case for oneplus one,Iphone, samsung,xiomi,micromax, oneplus one mobile case, back cover, kesi, phone cover, printed mobile case,back cover for oneplus one, Iphone, samsung,xiomi,micromax,printed back cover for oneplus one, oneplus one back cover, designer back cover, phone case,designer cover, mobile cover, 3d printed back cover for oneplus one, designer mobile case, back cover case, colourful mobile case,3d printed mobile covers, 3d printed back cover for oneplus one,Iphone, samsung,xiomi,micromax, oneplus one  mobile case,mobile case cover for  oneplus one,Iphone, samsung,xiomi,micromax, oneplus one , printed mobile cover for  oneplus one,Iphone, samsung,xiomi,micromax, oneplus one mobile cover'))
            row.append(cls.fill_image_url_in_row(product_image))
            
            cls.fill_empty_values_in_row(row, 4)
            row.append(cls.fill_package_height_in_row(package_height='5'))
            row.append(cls.fill_package_width_in_row(package_width='10'))
            row.append(cls.fill_package_length_in_row(package_length='18'))
            row.append(cls.fill_package_dimensions_unit_of_measure_in_row(package_dimensions_unit_of_measure='CM'))
            row.append(cls.fill_package_weight_in_row(package_weight='200'))
            row.append(cls.fill_package_weight_unit_of_measure_in_row(package_weight_unit_of_measure='GR'))
            
            cls.fill_empty_values_in_row(row, 0)
            writer.writerows(a)
    
    @classmethod
    def fill_empty_values_in_row(cls, a, count):
        if count < 1:
            col_len = constants.getAmazonCSVColumns()[0].__len__()
            a_len = a.__len__()
            for num in range(a_len, col_len):
                a.append("")
        else:
            for num in range(0, count):
                a.append("")
    
    @classmethod
    def get_sku(cls, phone_name):
        return "rucept" + str(time.time().real)
    
    @classmethod
    def fill_item_name_in_row(cls, dsn_image, phn_image):
        return '%s Printed Back Cover Case For %s' % (utils.strip_image_extensions(dsn_image), phn_image)
    @classmethod
    def fill_item_type_in_row(cls, item_type):
        return 'Phone Case'
    @classmethod
    def fill_brand_name_in_row(cls, brand):
        return 'KESI'
    
    @classmethod
    def fill_manufacturer_in_row(cls, y):
        return 'Rucept Designs'
    
    @classmethod
    def fill_product_description_in_row(cls, z):
        return 'Constructed with a plastic back, this case features a high quality printing. Snap it on the back of your phone to provide a robust protection, while keeping it colourful and classy. Made to fit Phone Case.'
    
    @classmethod
    def fill_feed_product_type_in_row(cls, xx):
        return 'PhoneAccessory'
    
    @classmethod
    def fill_update_delete_in_row(cls, update):
        return 'update'
    
    @classmethod
    def fill_currency_in_row(cls, currency):
        return 'INR'
    
    @classmethod
    def fill_quantity_in_row(cls, quantity):
        return '20'
    
    @classmethod
    def fill_condition_type_in_row(cls, cndttype):
        return 'New'
    
    @classmethod
    def fill_fulfillment_latency_in_row(cls, fulfillment):
        return '5'
    
    @classmethod
    def fill_item_dimensions_unit_of_measure_in_row(cls, item_dimensions_unit_of_measure):
        return 'CM'
    
    @classmethod
    def fill_item_weight_in_row(cls, item_weight):
        return '30'
    
    @classmethod
    def fill_item_weight_unit_of_measure_in_row(cls, item_weight_unit_of_measure):
        return 'GR'
    
    @classmethod
    def fill_bullet_point1_in_row(cls, bullet_point1):
        return 'Designed to fit Mobile Cases.'
    
    @classmethod
    def fill_bullet_point4_in_row(cls, bullet_point4):
        return 'Material: ABS Plastic.'
    
    @classmethod
    def fill_bullet_point2_in_row(cls, bullet_point2):
        return 'Protects your cell phone from scratches and dusts in daily use.'
    
    @classmethod
    def fill_bullet_point3_in_row(cls, bullet_point3):
        return 'High Quality 3D Printed Back Cover.'
    
    @classmethod
    def fill_bullet_point5_in_row(cls, bullet_point5):
        return 'Durable.'
    
    @classmethod
    def fill_recommended_browse_nodes_in_row(cls, recommended_browse_nodes):
        return '1389409031'
    
    @classmethod
    def fill_generic_keywords1_in_row(cls, generic_keywords1):
        return generic_keywords1
    
    @classmethod
    def fill_package_length_in_row(cls, package_length):
        return '18'
    
    @classmethod
    def fill_package_height_in_row(cls, package_height):
        return '5'
    
    @classmethod
    def fill_package_width_in_row(cls, package_width):
        return '10'
    
    @classmethod
    def fill_package_dimensions_unit_of_measure_in_row(cls, package_dimensions_unit_of_measure):
        return 'CM'
    
    @classmethod
    def fill_package_weight_in_row(cls, package_weight):
        return '200'
    
    @classmethod
    def fill_package_weight_unit_of_measure_in_row(cls, package_weight_unit_of_measure):
        return 'GR'
    
    @classmethod
    def fill_item_height_in_row(cls, item_height):
        return '0.71'
    
    @classmethod
    def fill_item_length_in_row(cls, item_length):
        return '13.83'
    
    @classmethod
    def fill_item_width_in_row(cls, item_width):
        return '6.71'
    
    @classmethod
    def fill_standard_price_in_row(cls, stndprice):
        return '24.99'
    
    @classmethod
    def fill_selling_price_in_row(cls, sellingprice):
        return '19.99'
    
    @classmethod
    def fill_sell_start_date_in_row(cls, startDate):
        return '2016-10-10'
    
    @classmethod
    def fill_sell_end_date_in_row(cls, endDate):
        return '2017-10-10'
    
    @classmethod
    def fill_image_url_in_row(cls, product_image):
        main_url = 'https://s3-us-west-2.amazonaws.com/rucept/'
        return main_url + product_image
    
    @classmethod
    def fill_modal_in_row(cls, phn_image):
        return utils.strip_image_extensions(phn_image)
    
    @classmethod
    def fill_type_in_row(cls, producttype):
        return 'Back Cover'
    
    @classmethod
    def fill_product_color_in_row(cls, productcolor):
        return 'Multi'
    
    @classmethod
    def fill_material_in_row(cls, productmaterial):
        return 'Plastic'
    
    @classmethod
    def fill_suitableDevice_in_row(cls, suitableDevice):
        return 'Mobile'
    
    @classmethod
    def fill_salesPackage_in_row(cls, salesPackage):
        return 'Back Cover'
    
    @classmethod
    def fill_productTheme_in_row(cls, productTheme):
        return 'No Theme'
    
    @classmethod
    def fill_brandColor_in_row(cls, brandColor):
        return 'Multi'
    
    @classmethod
    def fill_packOf_in_row(cls, packOf):
        return '1'
    
    @classmethod
    def fill_waterproof_in_row(cls, waterproof):
        waterproof = 'Yes'
        return (waterproof)
    
    #####################################################################################################################################
    #####################################################################################################################################
    #####################################################################################################################################
    @classmethod
    def generateFlipkartCSVs(cls, csv_out_path, csv_name, phone_name, dsn_image_name):
        filename = csv_out_path + "/" + csv_name
        if not os.path.exists(filename):
            cls.initCSV(csv_out_path, csv_name)
        
        with open(filename, "a") as file:
            writer = csv.writer(file)
            a = [[]]
            row = a[0]
            cls.fill_empty_values_in_row(row, 6)
            row.append(cls.get_sku(phone_name))
            row.append(cls.fill_brand_name_in_row(brand='Kesi'))
            row.append(cls.get_sku(phone_name))
            row.append(cls.fill_type_in_row(producttype='Back Cover'))
            row.append(cls.fill_product_color_in_row(productcolor='Multi'))
            row.append(cls.fill_modal_in_row(phn_image=phone_name))
            row.append(cls.fill_material_in_row(productmaterial='Plastic'))
            row.append(cls.fill_suitableDevice_in_row(suitableDevice='Mobile'))
            row.append(cls.fill_salesPackage_in_row(salesPackage='Back Cover'))
            row.append(cls.fill_productTheme_in_row(productTheme='No Theme'))
            row.append(cls.fill_brandColor_in_row(brandColor='Multi'))
            row.append(cls.fill_image_url_in_row(main_url='https://s3-us-west-2.amazonaws.com/rucept/octoutput/',
                                                 dsn_image=dsn_image_name, phn_image=phone_name))
            cls.fill_empty_values_in_row(row, 6)
            row.append(cls.fill_packOf_in_row(packOf='1'))
            row.append(cls.fill_product_description_in_row(
                z='Constructed with a plastic back, this case features a high quality printing. Snap it on the back of your phone to provide a robust protection, while keeping it colourful and classy. Made to fit Phone Case.'))
            row.append(cls.fill_generic_keywords1_in_row(
                generic_keywords1='case for oneplus one,Iphone, samsung,xiomi,micromax, oneplus one mobile case, back cover, kesi, phone cover, printed mobile case'))
            row.append(cls.fill_bullet_point1_in_row(bullet_point1='Designed to fit Phhones.'))
            row.append(cls.fill_bullet_point2_in_row(
                bullet_point2='Protects your cell phone from scratches and dusts in daily use.'))
            row.append(cls.fill_bullet_point3_in_row(bullet_point3='High Quality 3D Printed Back Cover.'))
            row.append(cls.fill_bullet_point4_in_row(bullet_point4='Material: ABS Plastic.'))
            row.append(cls.fill_bullet_point5_in_row(bullet_point5='Durable'))
            cls.fill_empty_values_in_row(row, 1)
            row.append(cls.fill_item_name_in_row(dsn_image_name, phone_name))
            cls.fill_empty_values_in_row(row, 2)
            row.append(cls.fill_waterproof_in_row(waterproof='Yes'))
            
            cls.fill_empty_values_in_row(row, 0)
            writer.writerows(a)
