import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'package:web_profile/widgets/home_screen.dart';

import 'app_styling.dart';

void main() {
  runApp(WebProfile());
}

class WebProfile extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Provider(
      create: (_) => AppStyling(),
      child: MaterialApp(
        title: 'Flutter Demo',
        theme: ThemeData(
          primarySwatch: MaterialColor(0xFF06B858, {
            50: Color(0xFF06B858),
            100: Color(0xFF06B858),
            200: Color(0xFF06B858),
            300: Color(0xFF06B858),
            400: Color(0xFF06B858),
            500: Color(0xFF06B858),
            600: Color(0xFF06B858),
            700: Color(0xFF06B858),
            800: Color(0xFF06B858),
            900: Color(0xFF06B858),
          }),
        ),
        home: HomeScreen(),
      ),
    );
  }
}
