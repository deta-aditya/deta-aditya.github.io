import 'package:flutter/material.dart';

import 'primary_button.dart';

class HeroSection extends StatelessWidget {
  const HeroSection({
    Key key,
  }) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Padding(
      padding: const EdgeInsets.symmetric(
        horizontal: 128.0,
        vertical: 200.0,
      ),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Text(
            "Hello, I'm",
            style: TextStyle(fontSize: 36),
          ),
          Text(
            "Deta Aditya",
            style: TextStyle(
              fontSize: 72,
              fontWeight: FontWeight.w600,
            ),
          ),
          Text(
            "I'm a software developer",
            style: TextStyle(
              fontSize: 36,
              fontWeight: FontWeight.w600,
            ),
          ),
          SizedBox(
            height: 48,
          ),
          PrimaryButton(
            onPressed: () {},
            text: "Contact Me",
          ),
        ],
      ),
    );
  }
}