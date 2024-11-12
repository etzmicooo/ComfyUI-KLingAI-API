from py.api import Client, Image2Video, Text2Video, ImageGenerator, CameraControl, CameraControlConfig, \
    KolorsVurtualTryOn
import traceback
import base64
import time


def image_to_base64(image_path):
    with open(image_path, "rb") as image_file:
        base64_encoded = base64.b64encode(image_file.read()).decode("utf-8")
    return base64_encoded


def test_text2video(client):
    text2Video = Text2Video()
    text2Video.model = 'kling-v1'
    text2Video.prompt = '夕阳下奔跑的骏马'
    text2Video.negative_prompt = '人'
    text2Video.cfg_scale = 0.8
    text2Video.mode = 'std'

    text2Video.camera_control = CameraControl()
    text2Video.camera_control.type = 'left_turn_forward'
    text2Video.aspect_ratio = '16:9'
    text2Video.duration = '5'
    print(text2Video.to_dict())

    ret = text2Video.run(client)
    print(ret)


def test_image2video(client):
    image2Video = Image2Video()
    image2Video.mode = "kling-v1"
    image2Video.image = image_to_base64('')
    image2Video.image_tail = image_to_base64('')
    image2Video.prompt = '夕阳下奔跑的骏马'
    image2Video.negative_prompt = '人'
    image2Video.cfg_scale = 1.0
    image2Video.mode = 'std'
    image2Video.duration = '5'

    ret = image2Video.run(client)
    print(ret)


def test_image_generator(client):
    imgGene = ImageGenerator()
    imgGene.n = 1
    imgGene.image_fidelity = 0.8
    imgGene.model = 'kling-v1'
    imgGene.prompt = '夕阳下奔跑的骏马'
    imgGene.negative_prompt = '人'
    print(imgGene.to_dict())

    ret = imgGene.run(client)
    print(ret)


def test_kolors_vurtual_try_on(client):
    generator = KolorsVurtualTryOn()
    generator.model_name = 'kolors-virtual-try-on-v1'
    generator.human_image = image_to_base64('')
    generator.cloth_image = image_to_base64('')
    print(generator.to_dict())

    ret = generator.run(client)
    print(ret)


if __name__ == '__main__':

    try:
        start_time = time.time()

        client = Client(access_key="",
                        secret_key="")

        test_image_generator(client)
        test_text2video(client)
        test_image2video(client)
        test_kolors_vurtual_try_on(client)

        elapsed_time = time.time() - start_time
        print(f"Elapsed time: {elapsed_time:.2f} seconds")

    except BaseException as e:

        print(f'exception: {e}')
        print(traceback.format_exc())


