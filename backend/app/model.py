# import clip
# import torch
from PIL import Image


def predict(img_path, classes):
    # device = "cuda" if torch.cuda.is_available() else "cpu"
    # model, preprocess = clip.load('ViT-B/32', device)

    # image = preprocess(Image.open(img_path)).unsqueeze(0).to(device)
    # text = clip.tokenize(classes).to(device)

    # with torch.no_grad():
    #     image_features = model.encode_image(image)
    #     text_features = model.encode_text(text)

    # image_features /= image_features.norm(dim=-1, keepdim=True)
    # text_features /= text_features.norm(dim=-1, keepdim=True)
    # similarity = (100.0 * image_features @ text_features.T).softmax(dim=-1)
    # if len(classes) >= 5:
    #     values, indices = similarity[0].topk(5)
    # else:
    #     values, indices = similarity[0].topk(len(classes))

    pred_classes = []
    pred_values = []

    # for value, index in zip(values, indices):
    #     pred_classes.append(classes[index])
    #     pred_values.append(100 * value.item())

    return {
        "classes": pred_classes,
        "values": pred_values
    }
