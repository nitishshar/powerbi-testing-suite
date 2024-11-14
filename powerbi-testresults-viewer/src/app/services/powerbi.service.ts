import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

export interface PowerBIModel {
  name: string;
  tables: PowerBITable[];
}

export interface PowerBITable {
  name: string;
  columns: PowerBIColumn[];
}

export interface PowerBIColumn {
  name: string;
  dataType: string;
}

@Injectable({
  providedIn: 'root'
})
export class PowerBIService {
  private apiUrl = 'http://localhost:8000/api/powerbi';

  constructor(private http: HttpClient) {}

  getModelSchema(): Observable<PowerBIModel> {
    return this.http.get<PowerBIModel>(`${this.apiUrl}/schema`);
  }
} 