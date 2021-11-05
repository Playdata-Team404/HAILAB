import 'package:flutter/material.dart';
import 'package:camera/camera.dart';
import 'package:flutter_auth/MainPage/Training/AIModel/AI_Camera.dart';
import 'package:flutter_auth/MainPage/Training/AIModel/render/Render_squat.dart';
import 'package:tflite/tflite.dart';
import 'dart:math';

class PoseSquat extends StatefulWidget {
  final int count;
  final List<CameraDescription> cameras;
  final String title;
  const PoseSquat({this.cameras, this.title, this.count});
  @override
  _PoseSquatState createState() => _PoseSquatState();
}

class _PoseSquatState extends State<PoseSquat> {
  List<dynamic> _data;
  int _imageHeight = 0;
  int _imageWidth = 0;
  int x = 1;

  @override
  void initState() {
    super.initState();
    var res = loadModel();
    print('Model Response: ' + res.toString());
  }

  _setRecognitions(data, imageHeight, imageWidth) {
    if (!mounted) {
      return;
    }
    setState(() {
      _data = data;
      _imageHeight = imageHeight;
      _imageWidth = imageWidth;
    });
  }

  loadModel() async {
    return await Tflite.loadModel(
        model: "assets/json/posenet_mv1_075_float_from_checkpoints.tflite");
  }

  @override
  Widget build(BuildContext context) {
    Size screen = MediaQuery.of(context).size;
    return Scaffold(
      // appBar: AppBar(
      //   title: Text('AlignAI Squat'),
      //   backgroundColor: Colors.transparent,
      //   elevation: 0,
      // ),
      body: SafeArea(
        child: Stack(
          children: <Widget>[
            PoseDetectCamera(
              cameras: widget.cameras,
              setRecognitions: _setRecognitions,
            ),
            RenderDataSquat(
              data: _data == null ? [] : _data,
              previewH: max(_imageHeight, _imageWidth),
              previewW: min(_imageHeight, _imageWidth),
              screenH: screen.height,
              screenW: screen.width,
              count: widget.count,
            ),
          ],
        ),
      ),
    );
  }
}
