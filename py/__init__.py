from .nodes import Text2VideoNode, ImageGeneratorNode, Image2VideoNode, KLingAIAPIClient, PreviewVideo, KolorsVirtualTryOnNode

NODE_CLASS_MAPPINGS = {
    'Client': KLingAIAPIClient,
    'Image Generator': ImageGeneratorNode,
    'Text2Video': Text2VideoNode,
    'Image2Video': Image2VideoNode,
    'Virtual Try On': KolorsVirtualTryOnNode,
    'KLingAI Preview Video': PreviewVideo
}