import pixellib
from pixellib.tune_bg import alter_bg
change_bg=alter_bg(model_type="pb")
change_bg.load_pascalvoc_model("xception_pascalvoc.pb")
change_bg.change_bg_img(f_image_path=r"C:\Users\VAIO\Desktop\art\1_.jpg",b_image_path=r"C:\Users\VAIO\Desktop\art\refined.jpg",output_image_name="hh.jpg")

